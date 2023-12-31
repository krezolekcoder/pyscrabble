import pygame
from board_config import *

class BoardController:
    def __init__(self):
        pass

    def get_tile_clicked_coords(self, x : int, y: int) -> (int, int):
        return ( int(x // (BOARD_WIDTH / BOARD_TILE_CNT)), int(y // (BOARD_WIDTH / BOARD_TILE_CNT)))

class BoardModel:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_TILE_CNT)] for _ in range(BOARD_TILE_CNT)] 

    def set_tile_letter(self, x_pos:int, y_pos:int, letter:str) -> bool:

        if len(letter) != 1:
            raise ValueError("String with len 1 required")
        
        if self.board[x_pos][y_pos] == None:
            self.board[x_pos][y_pos] = letter
            return True

class PlayerController():
    def __init__(self):
        pass 

class PlayerModel():

    def __init__(self, name:str, letters:str):
        self.score = 0
        self.letters = letters
        self.name = name
    
    def get_letters(self) -> str:
        pass

    def get_letter(self, letter) -> str:
        pass 

    def add_letter(self) -> str:
        pass

class BoardView:
    def __init__(self, model : BoardModel, player: PlayerModel):
        
        self.model = model
        self.color_matrix = [[TILE_DEFAULT_COLOR for _ in range(BOARD_TILE_CNT)] for _ in range(BOARD_TILE_CNT)]
        self.player = player
        
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
        self.tile_size = BOARD_WIDTH / BOARD_TILE_CNT  # Calculate tile size based on resolution and desired number of tiles
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        
        pygame.display.set_caption("SCRABBLE")

        # Set up font
        font_size = 60
        self.font = pygame.font.Font(None, font_size)


    def draw(self):
        self.screen.fill(WHITE_COLOR)

        for row in range(BOARD_TILE_CNT):
            for col in range(BOARD_TILE_CNT):
                # Calculate the position of each tile
                x = col * self.tile_size
                y = row * self.tile_size

                color = self.color_matrix[row][col]
                
                # Draw the tiles
                pygame.draw.rect(self.screen, color, (x, y, self.tile_size, self.tile_size))
                pygame.draw.rect(self.screen, BLACK_COLOR, (x, y, self.tile_size, self.tile_size), 1)  # 1 is the width of the border

        word_surfaces = self.__create_word_surfaces("SCRABBLE", (3, 7), HEADING_RIGHT)

        for surface, (x, y) in word_surfaces:
            rect = surface.get_rect(center=((x * self.tile_size) + self.tile_size/2, (y * self.tile_size) + self.tile_size/2))
            self.screen.blit(surface, rect)

        player_letters = self.__create_player_letter_surfaces(self.player.letters)
        
        for surface, coord in player_letters:
            x, y = coord 

            rect = surface.get_rect(center=((x * self.tile_size) + self.tile_size/2, (y * self.tile_size) + self.tile_size/2 + PLAYER_LETTERS_OFFSET))
            pygame.draw.rect(self.screen, BLACK_COLOR, ((x * self.tile_size), (y * self.tile_size) + PLAYER_LETTERS_OFFSET, self.tile_size, self.tile_size), 1)  # 1 is the width of the border
            self.screen.blit(surface, rect)

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
    
    def __create_player_letter_surfaces(self, letters: str) -> list:
        surfaces = []

        start_coord = (0, 15)
        heading = HEADING_RIGHT

        for idx, letter in enumerate(letters):

            surface = self.font.render(letter, True, BLACK_COLOR)

            coord = (start_coord[0] + idx * heading[0] , start_coord[1] + idx * heading[1])
            surfaces.append((surface, coord))

        return surfaces