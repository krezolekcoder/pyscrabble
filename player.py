from board_config import *
import pygame 



class PlayerModel():

    def __init__(self, name:str, letters:str):
        self.score = 0
        self.letters = [] 

        for letter in letters:
            self.letters.append([letter, False])

        print(self.letters)
        print(self.get_letters())
        self.name = name

    def player_letter_clicked(self, letter_idx):
        if self.letters[letter_idx][1]:
            self.letters[letter_idx][1] = False
        else:
            self.letters[letter_idx][1] = True

    
    def get_letters(self) -> str:
        
        letters = []

        for letter, _ in self.letters:
            letters.append(letter)

        return "".join(letters)

    def is_letter_clicked(self, letter_idx) -> bool:
        return self.letters[letter_idx][1]


class PlayerController:

    def __init__(self, player_model : PlayerModel):
        self.model = player_model
    
    def on_mouse_clicked(self, x :int, y:int):

        result = self.__get_tile_clicked_coords(x, y)

        if result == None:
            return
        
        x,y = result

        if y == 15 and x < len(self.model.get_letters()):
            self.model.player_letter_clicked(x)

    def __get_tile_clicked_coords(self, x : int, y: int) -> (int, int) or None:

        if y >= PLAYER_LETTERS_START_Y_COORD and x >= PLAYER_LETTERS_START_X_COORD:
            return (int((x - PLAYER_LETTERS_START_X_COORD) // (TILE_SIZE)), 15)
        
        elif y >= 0 and y < BOARD_HEIGHT and x >= 0 and x < BOARD_WIDTH:
            return ( int(x // (TILE_SIZE)), int(y // (TILE_SIZE)))
        else:
            return None
     
    
class PlayerView():

    def __init__(self, player_model:PlayerModel, screen):
        self.player = player_model 

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.screen = screen

    def draw(self):
        
        player_letters = self.__create_player_letter_surfaces(self.player.get_letters())
        
        for surface, coord in player_letters:
            x, y = coord 
            
            tile_color = WHITE_COLOR
            if self.player.is_letter_clicked(x):
                tile_color = TILE_DL_COLOR  

            rect = surface.get_rect(center=((x * TILE_SIZE) + TILE_SIZE/2 + LETTERS_X_OFFSET, (y * TILE_SIZE) + TILE_SIZE/2 + LETTERS_Y_OFFSET))
            pygame.draw.rect(self.screen, tile_color, ((x * TILE_SIZE) + LETTERS_X_OFFSET, (y * TILE_SIZE) + LETTERS_Y_OFFSET, TILE_SIZE, TILE_SIZE))            
            pygame.draw.rect(self.screen, BLACK_COLOR, ((x * TILE_SIZE) + LETTERS_X_OFFSET, (y * TILE_SIZE) + LETTERS_Y_OFFSET, TILE_SIZE, TILE_SIZE), 1)  # 1 is the width of the border
            self.screen.blit(surface, rect)

    
    def __create_player_letter_surfaces(self, letters: str) -> list:
        surfaces = []

        x, y = (0, 15)

        for idx, letter in enumerate(letters):
    
            surface = self.font.render(letter, True, BLACK_COLOR)

            coord = (x + idx * HEADING_RIGHT[0] , y + idx * HEADING_RIGHT[1])
            surfaces.append((surface, coord))

        return surfaces