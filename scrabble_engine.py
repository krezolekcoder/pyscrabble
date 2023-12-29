import numpy as np

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




def scrabble_engine_get_list_of_coords(word: str, start_coords : list):
    coords_dir = np.asarray(start_coords[1]) - np.asarray(start_coords[0])

    if 0 not in coords_dir or (coords_dir[0] > 1 or coords_dir[1] > 1):
        raise ValueError('Wrong start coords')
    
    coords_list = []

    for coord in range (0, len(word)):
        new_coord = np.asarray(np.asarray(start_coords[0]) + coord * coords_dir)
        coords_list.append(new_coord)

    return coords_list 


def scrabble_engine_calculate_score(word:str, start_coords : list):

    return 0 

