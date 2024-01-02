from board import *
from player import *
from controller import PlayerController
from engine import *
import pygame
import sys


if __name__ == "__main__":

    dictionary_path = sys.argv[1]

    scrabble_engine = Engine('letters_PL.json', 'dictionary_PL.txt')
    board_model = BoardModel()
    player_model = PlayerModel('Rocky', scrabble_engine.get_letters(7))
    player_controller = PlayerController(player_model, board_model, scrabble_engine)
    board_view = BoardView(board_model, player_model)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                player_controller.on_mouse_clicked(mouse_x, mouse_y)
        
        board_view.draw()
