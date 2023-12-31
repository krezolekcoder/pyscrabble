from board import *
from scrabble_engine import *
import pygame
import sys


if __name__ == "__main__":

    scrabble = ScrabbleGame('letters_PL.json')
    board_model = BoardModel()
    player = PlayerModel('Rocky', 'LITERY')

    board_view = BoardView(board_model, player)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # x, y = get_tile_clicked_coords(mouse_x, mouse_y, tile_size)
                # print(f"Mouse Click at ({mouse_x}, {mouse_y}) {get_tile_clicked_coords(mouse_x, mouse_y, tile_size)} ")
                # if y < 15:
                #     print(f"Tile ({x}, {y}) letter : {scrabble.get_tile_letter(x, y)}")
        
        board_view.draw()
