
import pygame
import random


pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 640, 512
GRID_ROWS, GRID_COLS = 16, 20
CELL_SIZE = 32
GRID_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (50, 50, 50)


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")


mole_image = pygame.image.load("mole.png")
mole_image = pygame.transform.scale(mole_image, (CELL_SIZE, CELL_SIZE))


mole_x, mole_y = 0, 0

def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

def draw_mole(x, y):
    screen.blit(mole_image, (x, y))

def get_random_position():
    col = random.randrange(0, GRID_COLS)
    row = random.randrange(0, GRID_ROWS)
    return col * CELL_SIZE, row * CELL_SIZE


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mole_x <= mouse_x < mole_x + CELL_SIZE and mole_y <= mouse_y < mole_y + CELL_SIZE:
                mole_x, mole_y = get_random_position()

    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    draw_mole(mole_x, mole_y)
    pygame.display.flip()

pygame.quit()
