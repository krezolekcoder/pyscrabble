from scrabble_engine import *
import pygame
import sys

if __name__ == "__main__":


    scrabble = ScrabbleGame('letters_PL.json')

    print(scrabble.score_matrix)
    
    # Initialize Pygame
    pygame.init()

    # Set up display
    resolution = (900, 900)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("SCRABBLE")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Board configuration
    tile_size = resolution[0] / 15  # Calculate tile size based on resolution and desired number of tiles

    # Create a 2D array to represent the board
    board = [[0] * 15 for _ in range(15)]

    # Draw the board
    screen.fill(white)

    for row in range(15):
        for col in range(15):
            # Calculate the position of each tile
            x = col * tile_size
            y = row * tile_size

            color = scrabble.score_matrix[row][col]
            
            # Draw the tiles
            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))
            pygame.draw.rect(screen, black, (x, y, tile_size, tile_size), 1)  # 2 is the width of the border

    # Update the display
    pygame.display.flip()
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

