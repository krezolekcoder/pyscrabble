from controller import *
from player import PlayerModel
from engine import Engine
from board import BoardModel


def test_controller_init():
    player_model = PlayerModel('przemek', 'domekwo')
    board_model = BoardModel()
    scrabble_engine = Engine('letters_PL.json', 'fake_dict.txt')

    controller = PlayerController(player_model, board_model, scrabble_engine)

    assert controller.player_sm.current_state == STATE_LETTER_CHOOSE

    # controller.handle_letter_choose_state(0, 15)

    