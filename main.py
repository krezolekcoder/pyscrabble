from scrabble_engine import *
from scrabble_player import *
import pygame
import sys



def get_tile_clicked_coords(mouse_x : int, mouse_y: int, tile_size : int) -> (int, int):
    return ( int(mouse_x // tile_size), int(mouse_y // tile_size))


# function that will create pygame surfaces for given word , starting coord and heading 

def create_word_surfaces(word: str, start_coord : tuple[int, int], heading:tuple[int, int]) -> list:

    if 0 not in heading or (heading[0] > 1 or heading[1] > 1):
            raise ValueError('Wrong heading')

    surfaces = []
    coords = start_coord 

    for idx, letter in enumerate(word):

        surface = font.render(letter, True, black)
        
        x = start_coord[0] + idx * heading[0]
        y = start_coord[1] + idx * heading[1]

        if x >= 0 and x < 15 and y >= 0 and y < 15:
            coord = (start_coord[0] + idx * heading[0] , start_coord[1] + idx * heading[1])
            scrabble.set_tile_letter(x, y, letter)
            surfaces.append((surface, coord))

    return surfaces

def create_player_letter_surfaces(letters: str) -> list:
    surfaces = []

    start_coord = (0, 15)
    heading = (1, 0)

    for idx, letter in enumerate(letters):

        surface = font.render(letter, True, black)
        
        # x = start_coord[0] + idx * heading[0]
        # y = start_coord[1] + idx * heading[1]

        coord = (start_coord[0] + idx * heading[0] , start_coord[1] + idx * heading[1])
        surfaces.append((surface, coord))

    return surfaces

PLAYER_LETTERS_OFFSET = 10

if __name__ == "__main__":

    scrabble = ScrabbleGame('letters_PL.json')
    player = Player('Rocky', 'LITERY')
    # Initialize Pygame
    pygame.init()

    width, height = 900, 1000
    # Set up display
    resolution = (width, height)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("SCRABBLE")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Board configuration
    tile_size = resolution[0] / 15  # Calculate tile size based on resolution and desired number of tiles

    # Create a 2D array to represent the board
    board = [[0] * 15 for _ in range(15)]

    # Set up font
    font_size = 60
    font = pygame.font.Font(None, font_size)

    word_surfaces = create_word_surfaces("SCRABBLE", (3,7), (1,0))



    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                x, y = get_tile_clicked_coords(mouse_x, mouse_y, tile_size)

                print(f"Mouse Click at ({mouse_x}, {mouse_y}) {get_tile_clicked_coords(mouse_x, mouse_y, tile_size)} ")

                if y < 15:
                    print(f"Tile ({x}, {y}) letter : {scrabble.get_tile_letter(x, y)}")
        
        screen.fill(white)

        for row in range(15):
            for col in range(15):
                # Calculate the position of each tile
                x = col * tile_size
                y = row * tile_size

                color = scrabble.color_matrix[row][col]
                
                # Draw the tiles
                pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))
                pygame.draw.rect(screen, black, (x, y, tile_size, tile_size), 1)  # 1 is the width of the border


        for surface, (x, y) in word_surfaces:
            rect = surface.get_rect(center=((x * tile_size) + tile_size/2, (y * tile_size) + tile_size/2))
            screen.blit(surface, rect)

        # Update player
            
        player_letters = create_player_letter_surfaces(player.letters)
        
        for surface, coord in player_letters:
            x, y = coord 

            rect = surface.get_rect(center=((x * tile_size) + tile_size/2, (y * tile_size) + tile_size/2 + PLAYER_LETTERS_OFFSET))
            pygame.draw.rect(screen, black, ((x * tile_size), (y * tile_size) + PLAYER_LETTERS_OFFSET, tile_size, tile_size), 1)  # 1 is the width of the border
            screen.blit(surface, rect)

        # Update the display
        pygame.display.flip()
