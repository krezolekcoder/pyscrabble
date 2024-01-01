from board_config import *
import pygame 



class PlayerModel():

    def __init__(self, name:str, letters:str):
        self.score = 0
        self.letters = [] 

        for letter in letters:
            self.letters.append([letter, False])

        self.name = name

    def player_letter_clicked(self, letter_idx):
        if self.letters[letter_idx][1]:
            self.letters[letter_idx][1] = False
        else:
            self.letters[letter_idx][1] = True

    
    def get_letter_clicked(self):

        for idx, (letter, clicked) in enumerate(self.letters):
            if clicked:
                return (letter, idx)
        

    def get_letters(self) -> str:
        
        letters = []

        for letter, _ in self.letters:
            letters.append(letter)

        return "".join(letters)

    def is_letter_clicked(self, letter_idx) -> bool:
        return self.letters[letter_idx][1]
    
    def remove_letter_at_idx(self, idx):
        print(f'Remove at idx {idx}')
        self.letters.pop(idx)



    
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