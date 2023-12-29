from scrabble_engine import *
import pytest

def test_coords_right():

    scrabble = ScrabbleGame("letters_PL.json")

    coords_list = scrabble.get_list_of_coords('OKO',  [[0, 0], [1, 0]])

    assert coords_list[2][0] == 2
    assert coords_list[2][1] == 0

def test_coords_left():

    scrabble = ScrabbleGame("letters_PL.json")

    coords_list = scrabble.get_list_of_coords('OKO', [[5, 0], [4, 0]])

    assert coords_list[2][0] == 3
    assert coords_list[2][1] == 0


def test_coords_up():

    scrabble = ScrabbleGame("letters_PL.json")

    coords_list = scrabble.get_list_of_coords('OKO', [[5, 7], [5, 6]])

    assert coords_list[2][0] == 5
    assert coords_list[2][1] == 5


def test_coords_down():

    scrabble = ScrabbleGame("letters_PL.json")

    coords_list = scrabble.get_list_of_coords('OKO', [[5, 5], [5, 6]])

    assert coords_list[2][0] == 5
    assert coords_list[2][1] == 7


def test_coords_error_input():
    scrabble = ScrabbleGame("letters_PL.json")

    with pytest.raises(ValueError, match='Wrong start coords') : scrabble.get_list_of_coords('OKO', [[5, 5], [5, 8]])


def test_word_score():
    scrabble = ScrabbleGame("letters_PL.json")

    score = scrabble.calculate_score("KOT", [[0, 4], [1, 4]])
    score_double_letter = scrabble.calculate_score("KOT", [[0, 3], [1, 3]])
    score_tripple_letter = scrabble.calculate_score("KOT", [[1, 5], [2, 5]])

    assert score == 5
    assert score_double_letter == 7
    assert score_tripple_letter == 9
