from scrabble_engine import *
import pygame
import sys

if __name__ == "__main__":

    print("SCRABLE")


    # scrabble = ScrabbleGame('letters_PL.json')

    # score = scrabble.calculate_score("KOT", [[0, 4], [1, 4]])
    # score = scrabble.calculate_score("KOT", [[0, 3], [1, 3]])
    # score = scrabble.calculate_score("KOT", [[1, 5], [2, 5]])

    
    # Initialize Pygame
    pygame.init()

    # Set up display
    resolution = (900, 900)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("15x15 Board")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    light_blue = (173, 216, 230)   # Light Blue (Sky Blue)
    deep_blue = (0, 0, 128)        # Deep Blue (Navy Blue)
    light_red = (255, 182, 193)     # Light Red (Light Pink)
    deep_red = (139, 0, 0)          # Deep Red (Dark Red)

    # Board configuration
    tile_size = resolution[0] // 15  # Calculate tile size based on resolution and desired number of tiles

    # Create a 2D array to represent the board
    board = [[0] * 15 for _ in range(15)]

    # Draw the board
    screen.fill(white)

    for row in range(15):
        for col in range(15):
            # Calculate the position of each tile
            x = col * tile_size
            y = row * tile_size

            # Draw the tiles
            pygame.draw.rect(screen, black, (x, y, tile_size, tile_size), 1)

    # Update the display
    pygame.display.flip()
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

