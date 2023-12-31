import numpy as np
import json

TRIPLE_WORD_SCORE_COORDS = ((0, 0), (7, 0), (14, 0), 
                           (0, 7), (14, 7),
                           (0, 14), (7, 14), (14, 14))

DOUBLE_WORD_SCORE_COORDS = ((1, 1), (2, 2), (3, 3), (4, 4),
                            (13, 1), (12, 2), (11, 3), (10, 4),
                            (4, 10), (3, 11), (2, 12), (1, 13),
                            (13, 13), (12, 12), (11, 11), (10, 10))

TRIPLE_LETTER_SCORE_COORDS = ((5, 1), (9, 1),
                              (1, 5), (5, 5), (9, 5), (13,5),
                              (1, 9), (5, 9), (9, 9), (13,9),
                              (5, 13), (9, 13))

DOUBLE_LETTER_SCORE_COORDS = ((3, 0), (11, 0),
                              (6, 2), (8, 2), 
                              (0, 3), (7, 3), (14, 3),
                              (2, 6), (6, 6), (8, 6), (12, 6), 
                              (3, 7), (11, 7),
                              (2, 8), (6, 8), (8, 8), (12, 8),
                              (0, 11), (7, 11), (14, 11),
                              (6, 12), (8, 12),
                              (3, 14), (11, 14))


TILE_DL_COLOR = (173, 216, 230)   # Light Blue (Sky Blue)
TILE_TL_COLOR =  (70, 130, 180)    # Deep Blue (Navy Blue)
TILE_DW_COLOR = (255, 182, 193)     # Light Red (Light Pink)
TILE_TW_COLOR = (220, 20, 60)          # Deep Red (Dark Red)
TILE_DEFAULT_COLOR = (255, 255, 255) # white 
 
class ScrabbleGame():

    def __init__(self, json_config_path : str):
        with open(json_config_path, 'r', encoding='utf-8') as file:
            # Load the JSON data
            self.config = json.load(file)

        self.color_matrix = [[TILE_DEFAULT_COLOR for _ in range(15)] for _ in range(15)]
        self.score_mult = [[("N", 1) for _ in range(15)] for _ in range(15)]
        self.board = [[None for _ in range(15)] for _ in range(15)]

        for coord in TRIPLE_WORD_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_TW_COLOR
            self.score_mult[coord[0]][coord[1]] = ("W", 3)

        for coord in DOUBLE_WORD_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_DW_COLOR
            self.score_mult[coord[0]][coord[1]] = ("W", 2)
        
        for coord in TRIPLE_LETTER_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_TL_COLOR
            self.score_mult[coord[0]][coord[1]] = ("L", 3)

        for coord in DOUBLE_LETTER_SCORE_COORDS:
            self.color_matrix[coord[0]][coord[1]] = TILE_DL_COLOR
            self.score_mult[coord[0]][coord[1]] = ("L", 2)

    def set_tile_letter(self, x_pos:int, y_pos:int, letter:str) -> bool:

        if len(letter) != 1:
            raise ValueError("String with len 1 required")
        
        if self.board[x_pos][y_pos] == None:
            self.board[x_pos][y_pos] = letter
            return True
        

    def get_tile_letter(self, x_pos:int, y_pos:int) -> str or None:
        return self.board[x_pos][y_pos]

    def calculate_score(self, word:str, start_coord : tuple[int, int], heading : tuple[int, int]):
        
        coords_list = self.__get_list_of_coords(word, start_coord, heading) 

        score = 0

        word_multipliers = []

        for coord, letter in zip(coords_list, word):
            letter_score = self.config["tiles_score"][letter]

            mult_type, mult_value = self.score_mult[coord[0]][coord[1]]

            if mult_type == "L":
                letter_score *= mult_value
            elif mult_type == "W":
                word_multipliers.append(mult_value)

            score += letter_score

        for mult in word_multipliers:
            score *= mult

        return score

    def __get_list_of_coords(self, word: str, start_coord: tuple[int, int], heading: tuple[int, int]):
        
        if 0 not in heading or (heading[0] > 1 or heading[1] > 1):
            raise ValueError('Wrong heading')
        
        ## add check if word fits in board with given start coord, len and heading 

        coords_list = []

        for coord in range (0, len(word)):

            x = start_coord[0] + coord * heading[0]
            y = start_coord[1] + coord * heading[1]

            # new_coord = np.asarray(np.asarray(start_coords[0]) + coord * coords_dir)
            coords_list.append((x, y))

        return coords_list 
