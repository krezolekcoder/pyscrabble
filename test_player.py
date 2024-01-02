from player import PlayerModel
from board_config import *

def test_player_word_letters_first_letter():

    player = PlayerModel('Helo', 'LITERAKI')

    result = player.player_add_word_letter('A', (5, 5))

    assert result == True
    assert player.current_word_letters[0][0] == 'A'
    assert player.current_word_letters[0][1][0] == 5
    assert player.current_word_letters[0][1][1] == 5


def test_player_word_letters_check_heading():

    player = PlayerModel('Helo', 'LITERAKI')

    player.player_add_word_letter('A', (5,5))
    player.player_add_word_letter('B', (5,6))

    assert player.current_word_heading[0] == HEADING_DOWN[0]
    assert player.current_word_heading[1] == HEADING_DOWN[1]

    player.current_word_letter = []

    player.player_add_word_letter('A', (5, 5))
    player.player_add_word_letter('B', (4, 5))

    assert player.current_word_heading[0] == HEADING_LEFT[0]
    assert player.current_word_heading[1] == HEADING_LEFT[1]

    player.current_word_letter = []

    player.player_add_word_letter('A', (5, 5))
    player.player_add_word_letter('B', (6, 5))

    assert player.current_word_heading[0] == HEADING_RIGHT[0]
    assert player.current_word_heading[1] == HEADING_RIGHT[1]

    player.current_word_letter = []

    player.player_add_word_letter('A', (5, 6))
    player.player_add_word_letter('B', (5, 5))

    assert player.current_word_heading[0] == HEADING_UP[0]
    assert player.current_word_heading[1] == HEADING_UP[1]