import numpy as np
import json

TRIPLE_WORD_SCORE_COORDS = ((0, 0), (7, 0), (14, 0), 
                           (0, 7), (14, 7),
                           (0, 14), (7, 14), (14, 14))

DOUBLE_WORD_SCORE_COORDS = ((1, 1), (2, 2), (3, 3), (4, 4),
                            (14, 1), (13, 2), (12, 3), (11, 4),
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


class ScrabbleGame():

    def __init__(self, json_config_path : str):
        with open(json_config_path, 'r', encoding='utf-8') as file:
            # Load the JSON data
            self.config = json.load(file)
    
    def calculate_score(self, word:str, start_coords : list[int, int]):
        
        coords_list = self.get_list_of_coords(word, start_coords) 

        score = 0

        for coord, letter in zip(coords_list, word):
            letter_score = self.config["tiles_score"][letter]

            for dbl_coord in DOUBLE_LETTER_SCORE_COORDS :
                converted_coord = np.array([dbl_coord])[0]

                if converted_coord[0] == coord[0] and converted_coord[1] == coord[1]:
                    print('Double letter score')
                    letter_score *= 2

            for trp_coord in TRIPLE_LETTER_SCORE_COORDS:
                converted_coord = np.array([trp_coord])[0]

                if converted_coord[0] == coord[0] and converted_coord[1] == coord[1]:
                    print('Triple letter score')
                    letter_score *= 3
            

            score += letter_score



        return score

    def get_list_of_coords(self, word: str, start_coords: list):
        coords_dir = np.asarray(start_coords[1]) - np.asarray(start_coords[0])

        if 0 not in coords_dir or (coords_dir[0] > 1 or coords_dir[1] > 1):
            raise ValueError('Wrong start coords')
        
        coords_list = []

        for coord in range (0, len(word)):
            new_coord = np.asarray(np.asarray(start_coords[0]) + coord * coords_dir)
            coords_list.append(new_coord)

        return coords_list 
        