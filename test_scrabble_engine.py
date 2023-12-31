from scrabble_engine import *
import pytest


def test_word_score():
    scrabble = ScrabbleGame("letters_PL.json")

    score = scrabble.calculate_score("KOT", (0, 4), (1, 0))
    score_double_letter = scrabble.calculate_score("KOT", (0, 3), (0, 1))
    score_tripple_letter = scrabble.calculate_score("KOT", (1, 5), (1, 0))

    assert score == 5
    assert score_double_letter == 7
    assert score_tripple_letter == 9
