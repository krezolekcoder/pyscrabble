from scrabble_engine import *
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






if __name__ == "__main__":

    scrabble = ScrabbleGame('letters_PL.json')
    
    # Initialize Pygame
    pygame.init()

    width, height = 900, 900
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


    # popup rectangle with letters
    popup_size = 200 
    popup_color = (255, 0, 0)
    popup_rect = pygame.Rect(0, 0, popup_size, popup_size)
    popup_rect.center = screen.get_rect().center

    show_popup = False

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

                print(f"Tile ({x}, {y}) letter : {scrabble.get_tile_letter(x, y)}")

                # if show_popup == False:
                #     show_popup = True
                # else:
                #     show_popup = False 
        
        screen.fill(white)

        for row in range(15):
            for col in range(15):
                # Calculate the position of each tile
                x = col * tile_size
                y = row * tile_size

                color = scrabble.color_matrix[row][col]
                
                # Draw the tiles
                pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))
                pygame.draw.rect(screen, black, (x, y, tile_size, tile_size), 1)  # 2 is the width of the border


        for surface, coord in word_surfaces:

            rect = surface.get_rect(center=((coord[0] * tile_size) + tile_size/2, (coord[1] * tile_size) + tile_size/2))
            screen.blit(surface, rect)

        if show_popup:
            pygame.draw.rect(screen, popup_color, popup_rect)

        # Update the display
        pygame.display.flip()
