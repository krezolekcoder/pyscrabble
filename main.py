from board import *
from player import *
from controller import PlayerController
from scrabble_engine import *
import pygame
import sys


if __name__ == "__main__":

    scrabble = ScrabbleGame('letters_PL.json')
    board_model = BoardModel()
    player_model = PlayerModel('Rocky', 'TALLIN')
    player_controller = PlayerController(player_model, board_model)
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
