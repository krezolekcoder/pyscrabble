from board_config import *
import pygame 

class PlayerController:

    def __init__(self):
        pass
    
    def on_mouse_clicked(self, x :int, y:int):
        x, y = self.__get_tile_clicked_coords(x, y)
        print(x, y)

    def __get_tile_clicked_coords(self, x : int, y: int) -> (int, int):
        return ( int(x // (BOARD_WIDTH / BOARD_TILE_CNT)), int(y // (BOARD_WIDTH / BOARD_TILE_CNT)))


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


class PlayerView():

    def __init__(self, player_model:PlayerModel, screen):
        self.player = player_model 

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.screen = screen

    def draw(self):
        
        player_letters = self.__create_player_letter_surfaces(self.player.letters)
        
        for surface, coord in player_letters:
            x, y = coord 

            rect = surface.get_rect(center=((x * TILE_SIZE) + TILE_SIZE/2, (y * TILE_SIZE) + TILE_SIZE/2 + PLAYER_LETTERS_OFFSET))
            pygame.draw.rect(self.screen, BLACK_COLOR, ((x * TILE_SIZE), (y * TILE_SIZE) + PLAYER_LETTERS_OFFSET, TILE_SIZE, TILE_SIZE), 1)  # 1 is the width of the border
            self.screen.blit(surface, rect)

    
    def __create_player_letter_surfaces(self, letters: str) -> list:
        surfaces = []

        start_coord = (0, 15)
        heading = HEADING_RIGHT

        for idx, letter in enumerate(letters):

            surface = self.font.render(letter, True, BLACK_COLOR)

            coord = (start_coord[0] + idx * heading[0] , start_coord[1] + idx * heading[1])
            surfaces.append((surface, coord))

        return surfaces