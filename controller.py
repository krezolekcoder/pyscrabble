from board import BoardModel
from player import PlayerModel
from board_config import *
from engine import Engine

STATE_LETTER_CHOOSE = "LETTER_CHOOSE"
STATE_LETTER_CHOSEN = "LETTER_CHOSEN"
STATE_WORD_PLACED = "WORD_PLACED"


class PlayerStateMachine:
    def __init__(self, initial_state, player_model: PlayerModel, board_model: BoardModel):
        self.current_state = initial_state


class PlayerController:

    def __init__(self, player_model : PlayerModel, board_model : BoardModel, scrabble_engine : Engine):
        self.model = player_model
        self.board = board_model
        self.player_sm = PlayerStateMachine(STATE_LETTER_CHOOSE, self.model, self.board)
        self.engine = scrabble_engine

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

        elif y == 15 and x == idx:
            self.model.player_letter_clicked(x)
            self.player_sm.current_state = STATE_LETTER_CHOOSE


    def handle_word_placed_state(self, x: int, y:int):
        
        print(f'Word placed! ')

        self.player_sm.current_state = STATE_LETTER_CHOOSE

        letters_to_get = 7 - len(self.model.letters)

        new_letters = self.engine.get_letters(letters_to_get)

        for letter in new_letters:
            self.model.player_add_hand_letter(letter)
        
        self.model.current_word_letters = []

    
    def __get_tile_clicked_coords(self, x : int, y: int) -> (int, int) or None:

        if y >= PLAYER_LETTERS_START_Y_COORD and x >= PLAYER_LETTERS_START_X_COORD:
            return (int((x - PLAYER_LETTERS_START_X_COORD) // (TILE_SIZE)), 15)
        elif y >= 0 and y < BOARD_HEIGHT and x >= 0 and x < BOARD_WIDTH:
            return ( int(x // (TILE_SIZE)), int(y // (TILE_SIZE)))
        else:
            return None

