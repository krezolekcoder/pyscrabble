from engine import *
import pytest
import time

def test_engine_init():
    scrabble = Engine("letters_PL.json", 'fake_dict.txt')

    total_cnt = len(scrabble.letters)

    assert total_cnt == 100

def test_engine_letters_pop():
    scrabble = Engine("letters_PL.json", 'fake_dict.txt')

    random_letters = scrabble.get_letters(7)

    print(random_letters)
    assert len(scrabble.letters) == 100 - 7

def test_word_score():
    scrabble = Engine("letters_PL.json", 'fake_dict.txt')

    score = scrabble.calculate_score("KOT", (0, 4), (1, 0))
    score_double_letter = scrabble.calculate_score("KOT", (0, 3), (0, 1))
    score_tripple_letter = scrabble.calculate_score("KOT", (1, 5), (1, 0))

    assert score == 5
    assert score_double_letter == 7
    assert score_tripple_letter == 9


def test_word_check():

    scrabble = Engine("letters_PL.json", 'dictionary_PL.txt')

    assert scrabble.is_word_in_dictionary("lody") == True
    assert scrabble.is_word_in_dictionary("GLOBUS") == True
    assert scrabble.is_word_in_dictionary("Bebeb") == False
