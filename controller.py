from board import BoardModel
from player import PlayerModel
from board_config import *

STATE_LETTER_CHOOSE = "LETTER_CHOOSE"
STATE_LETTER_CHOSEN = "LETTER_CHOSEN"
STATE_WORD_PLACED = "WORD_PLACED"


class PlayerStateMachine:
    def __init__(self, initial_state, player_model: PlayerModel, board_model: BoardModel):
        self.player_model = player_model
        self.board_model = board_model
        self.current_state = initial_state

        self.transitions = {
            "LETTER_CHOOSE": self.handle_letter_choose, 
            "LETTER_CHOSEN": self.handle_letter_chosen,
            "LETTER_PLACED": self.handle_letter_placed
        }

    def transition(self, new_state):
        print(f"Transitioning from {self.current_state} to {new_state}")
        handler = self.transitions.get(new_state)
        if handler:
            handler()
            self.current_state = new_state
        else:
            print(f"No transition handler found for state {new_state}")


    def handle_letter_choose(self, x, y):
        pass

    def handle_letter_chosen(self):
        pass

    def handle_letter_placed(self):
        pass



class PlayerController:

    def __init__(self, player_model : PlayerModel, board_model : BoardModel):
        self.model = player_model
        self.board = board_model
        self.player_sm = PlayerStateMachine(STATE_LETTER_CHOOSE, self.model, self.board)
    
    def on_mouse_clicked(self, x :int, y:int):
        
        result = self.__get_tile_clicked_coords(x, y)

        if result == None:
            return
    
        x,y = result
        
        if self.player_sm.current_state == STATE_LETTER_CHOOSE:
            self.handle_letter_choose_state(x, y)
        elif self.player_sm.current_state == STATE_LETTER_CHOSEN:
            self.handle_letter_chosen_state(x, y)
        elif self.player_sm.current_state == STATE_WORD_PLACED:
            self.handle_word_placed_state(x, y)
        else:
            pass 

    def handle_letter_choose_state(self, x : int, y: int):

        for idx, (letter, (x_pos, y_pos)) in enumerate(self.model.current_word_letters):
            if x == x_pos and y == y_pos and letter != None:
                self.board.reset_tile_letter(x, y)
                self.model.player_add_hand_letter(letter)
                self.model.current_word_letters.pop(idx)

        if y == 15 and x < len(self.model.get_letters()):
            self.model.player_letter_clicked(x)
            self.player_sm.current_state = STATE_LETTER_CHOSEN
        
        elif x == BUTTON_GREEN[0] and y == BUTTON_GREEN[1] and len(self.model.current_word_letters) >= 2:
            print(f'Word proposed : {self.model.current_word_letters}')
            self.player_sm.current_state = STATE_WORD_PLACED

    def handle_letter_chosen_state(self, x: int, y:int):
        letter, idx = self.model.get_letter_clicked()


        if x >= 0 and x < 15 and y >= 0 and y < 15:
            if self.model.player_add_word_letter(letter, (x, y)) :
                if self.board.set_tile_letter(x, y, letter):
                    self.model.remove_letter_at_idx(idx)
                    self.player_sm.current_state = STATE_LETTER_CHOOSE
                else:
                    print('Wrong tile ')
            else:
                print(f"Tile occupied : letter {self.board.board[x][y]}")

        elif y == 15 and x == idx:
            self.model.player_letter_clicked(x)
            self.player_sm.current_state = STATE_LETTER_CHOOSE

        print(self.model.current_word_letters)


    def handle_word_placed_state(self, x: int, y:int):
        
        print(f'Word placed! ')

        self.player_sm.current_state = STATE_LETTER_CHOOSE
        self.model.current_word_letters = []

    
    def __get_tile_clicked_coords(self, x : int, y: int) -> (int, int) or None:

        if y >= PLAYER_LETTERS_START_Y_COORD and x >= PLAYER_LETTERS_START_X_COORD:
            return (int((x - PLAYER_LETTERS_START_X_COORD) // (TILE_SIZE)), 15)
        elif y >= 0 and y < BOARD_HEIGHT and x >= 0 and x < BOARD_WIDTH:
            return ( int(x // (TILE_SIZE)), int(y // (TILE_SIZE)))
        else:
            return None

