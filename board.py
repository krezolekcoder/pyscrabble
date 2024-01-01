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
        
    def reset_tile_letter(self, x_pos:int, y_pos:int):
        self.board[x_pos][y_pos] = None 
        


class BoardView:
    def __init__(self, model : BoardModel, player: PlayerModel):
        
        self.board_model = model
        self.player = player 
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

        
        pygame.draw.rect(self.screen, (0, 255, 0), (BUTTON_GREEN_COORDS[0], BUTTON_GREEN_COORDS[1], TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.screen, BLACK_COLOR, (BUTTON_GREEN_COORDS[0], BUTTON_GREEN_COORDS[1], TILE_SIZE, TILE_SIZE), 1)

        pygame.draw.rect(self.screen, (255, 0, 0), (BUTTON_RED_COORDS[0], BUTTON_RED_COORDS[1], TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.screen, BLACK_COLOR, (BUTTON_RED_COORDS[0], BUTTON_RED_COORDS[1], TILE_SIZE, TILE_SIZE), 1)
                
        for surface, (x,y) in self.__create_letters_surfaces():
            rect = surface.get_rect(center=((x * TILE_SIZE) + TILE_SIZE/2, (y * TILE_SIZE) + TILE_SIZE/2))
            self.screen.blit(surface, rect) 

        self.player_view.draw()

        pygame.display.flip()

    def __create_letters_surfaces(self) -> list:
        
        surfaces = []

        # for coord, letter in self.board_model.board
        for x, row in enumerate(self.board_model.board):
            for y, element in enumerate(row):
                if element != None:
                    surface = self.font.render(element, True, BLACK_COLOR)
                    surfaces.append((surface, (x, y)))

        return surfaces


    
