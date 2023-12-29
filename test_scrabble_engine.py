from scrabble_engine import *
import pytest

def test_coords_right():

    coords_list = scrabble_engine_get_list_of_coords('OKO',  [[0, 0], [1, 0]])

    assert coords_list[2][0] == 2
    assert coords_list[2][1] == 0

def test_coords_left():

    coords_list = scrabble_engine_get_list_of_coords('OKO', [[5, 0], [4, 0]])

    assert coords_list[2][0] == 3
    assert coords_list[2][1] == 0


def test_coords_up():

    coords_list = scrabble_engine_get_list_of_coords('OKO', [[5, 7], [5, 6]])

    assert coords_list[2][0] == 5
    assert coords_list[2][1] == 5


def test_coords_down():

    coords_list = scrabble_engine_get_list_of_coords('OKO', [[5, 5], [5, 6]])

    assert coords_list[2][0] == 5
    assert coords_list[2][1] == 7


def test_coords_error_input():
    with pytest.raises(ValueError, match='Wrong start coords') : scrabble_engine_get_list_of_coords('OKO', [[5, 5], [5, 8]])