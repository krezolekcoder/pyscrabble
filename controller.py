from board import BoardModel
from player import PlayerModel
from board_config import *

class PlayerController:

    def __init__(self, player_model : PlayerModel, board_model : BoardModel):
        self.model = player_model
        self.board = board_model
        self.state = "LETTER_CLICK_WAIT"
    
    def on_mouse_clicked(self, x :int, y:int):
    
        result = self.__get_tile_clicked_coords(x, y)

        if result == None:
            return
    
        x,y = result

        if self.state == "LETTER_CLICK_WAIT":
            if y == 15 and x < len(self.model.get_letters()):
                self.model.player_letter_clicked(x)
                self.state = "BOARD_CLICK_WAIT"

        elif self.state == "BOARD_CLICK_WAIT":
            if x >= 0 and x < 15 and y >= 0 and y < 15:
                letter_clicked = self.model.get_letter_clicked()
                
                if self.board.set_tile_letter(x, y, letter_clicked):
                    print(f"Tile {x} {y} letter {letter_clicked} ")
                else:
                    print(f"Tile occupied : letter {self.board.board[x][y]}")


    def __get_tile_clicked_coords(self, x : int, y: int) -> (int, int) or None:

        if y >= PLAYER_LETTERS_START_Y_COORD and x >= PLAYER_LETTERS_START_X_COORD:
            return (int((x - PLAYER_LETTERS_START_X_COORD) // (TILE_SIZE)), 15)
        
        elif y >= 0 and y < BOARD_HEIGHT and x >= 0 and x < BOARD_WIDTH:
            return ( int(x // (TILE_SIZE)), int(y // (TILE_SIZE)))
        else:
            return None
     