import numpy as np
import json
from board_config import TRIPLE_WORD_SCORE_COORDS, TRIPLE_LETTER_SCORE_COORDS, DOUBLE_LETTER_SCORE_COORDS, DOUBLE_WORD_SCORE_COORDS

 
class ScrabbleGame():

    def __init__(self, json_config_path : str):
        with open(json_config_path, 'r', encoding='utf-8') as file:
            # Load the JSON data
            self.config = json.load(file)

        self.score_mult = [[("N", 1) for _ in range(15)] for _ in range(15)]
        self.board = [[None for _ in range(15)] for _ in range(15)]

        for coord in TRIPLE_WORD_SCORE_COORDS:
            self.score_mult[coord[0]][coord[1]] = ("W", 3)

        for coord in DOUBLE_WORD_SCORE_COORDS:
            self.score_mult[coord[0]][coord[1]] = ("W", 2)
        
        for coord in TRIPLE_LETTER_SCORE_COORDS:
            self.score_mult[coord[0]][coord[1]] = ("L", 3)

        for coord in DOUBLE_LETTER_SCORE_COORDS:
            self.score_mult[coord[0]][coord[1]] = ("L", 2)

    def calculate_score(self, word:str, start_coord : tuple[int, int], heading : tuple[int, int]):
        
        coords_list = self.__get_list_of_coords(word, start_coord, heading) 

        score = 0

        word_multipliers = []

        for (x, y), letter in zip(coords_list, word):
            letter_score = self.config["tiles_score"][letter]

            mult_type, mult_value = self.score_mult[x][y]

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

            coords_list.append((x, y))

        return coords_list 
