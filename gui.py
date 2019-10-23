import pygame
import random

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVY = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

WIDTH = 360
HEIGHT = 480
FPS = 30
BGCOLOR = BLACK

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Artificial Intelligence")

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    # Game loop part 1: Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # add any other events here (keys, mouse, etc.)

    # Game loop part 2: Updates

    # Game loop part 3: Draw
    screen.fill(BGCOLOR)

    # after drawing, flip the display
    pygame.display.flip()

# close the window
pygame.quit()