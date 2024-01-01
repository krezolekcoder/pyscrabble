import pygame
from board_config import *
from player import PlayerModel, PlayerView


class BoardModel:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_TILE_CNT)] for _ in range(BOARD_TILE_CNT)] 

    def set_tile_letter(self, x_pos:int, y_pos:int, letter:str) -> bool:

        if len(letter) != 1:
            raise ValueError("String with len 1 required")
        
        if self.board[x_pos][y_pos] == None:
            self.board[x_pos][y_pos] = letter
            return True


class BoardView:
    def __init__(self, model : BoardModel, player: PlayerModel):
        
        self.model = model
        self.color_matrix = [[TILE_DEFAULT_COLOR for _ in range(BOARD_TILE_CNT)] for _ in range(BOARD_TILE_CNT)]
        
        for coord in TRIPLE_WORD_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_TW_COLOR

        for coord in DOUBLE_WORD_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_DW_COLOR
        
        for coord in TRIPLE_LETTER_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_TL_COLOR

        for coord in DOUBLE_LETTER_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_DL_COLOR

        # Initialize Pygame
        pygame.init()
        # Set up display
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        pygame.display.set_caption("SCRABBLE")

        self.font = pygame.font.Font(None, FONT_SIZE)

        self.player = player 
        self.player_view = PlayerView(self.player, self.screen)


    def draw(self):
        self.screen.fill(WHITE_COLOR)

        for row in range(BOARD_TILE_CNT):
            for col in range(BOARD_TILE_CNT):
                # Calculate the position of each tile
                x = col * TILE_SIZE
                y = row * TILE_SIZE

                color = self.color_matrix[row][col]
                
                # Draw the tiles
                pygame.draw.rect(self.screen, color, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 1)  # 1 is the width of the border

        word_surfaces = self.__create_word_surfaces("SCRABBLE", (3, 7), HEADING_RIGHT)

        for surface, (x, y) in word_surfaces:
            rect = surface.get_rect(center=((x * TILE_SIZE) + TILE_SIZE/2, (y * TILE_SIZE) + TILE_SIZE/2))
            self.screen.blit(surface, rect)

        self.player_view.draw()

        pygame.display.flip()

    def __create_word_surfaces(self, word: str, start_coord : tuple[int, int], heading:tuple[int, int]) -> list:

        if 0 not in heading or (heading[0] > 1 or heading[1] > 1):
                raise ValueError('Wrong heading')

        surfaces = []

        for idx, letter in enumerate(word):

            surface = self.font.render(letter, True, BLACK_COLOR)
            
            x = start_coord[0] + idx * heading[0]
            y = start_coord[1] + idx * heading[1]

            if x >= 0 and x < 15 and y >= 0 and y < 15:
                coord = (start_coord[0] + idx * heading[0] , start_coord[1] + idx * heading[1])
                self.model.set_tile_letter(x, y, letter)
                surfaces.append((surface, coord))

        return surfaces
    