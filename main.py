from scrabble_engine import *

if __name__ == "__main__":

    print("SCRABLE")


    scrabble = ScrabbleGame('letters_PL.json')

    score = scrabble.calculate_score("KOT", [[0, 4], [1, 4]])
    score = scrabble.calculate_score("KOT", [[0, 3], [1, 3]])
    score = scrabble.calculate_score("KOT", [[1, 5], [2, 5]])
