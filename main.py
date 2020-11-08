import pygame
from pygame.locals import *
pygame.init()

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pato-man")

# Set Pacman object and image
pacman_obj = (10,10)
pacman_img = pygame.Surface((10,10))
pacman_img.fill((255,255,0))

# Start Direction
my_direction = RIGHT

# Clock Speed
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(25)
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            running = False

        # Directions keys
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    # Screen
    screen.fill((0, 0, 0))

    # Directions update
    if my_direction == UP:
        pacman_obj = (pacman_obj[0],pacman_obj[1]-10)
    if my_direction == RIGHT:
        pacman_obj = (pacman_obj[0]+10,pacman_obj[1])
    if my_direction == DOWN:
        pacman_obj = (pacman_obj[0], pacman_obj[1]+10)
    if my_direction == LEFT:
        pacman_obj = (pacman_obj[0]-10, pacman_obj[1])

    # End of screen ( Para não sair da tela e aparecer do lado oposto)
    if pacman_obj[0] < 0:
        pacman_obj = (790,pacman_obj[1])
    if pacman_obj[1] < 0:
        pacman_obj = (pacman_obj[0], 590)
    if pacman_obj[0] >= 800:
        pacman_obj = (10,pacman_obj[1])
    if pacman_obj[1] >= 600:
        pacman_obj = (pacman_obj[0],10)

    # Object on screen
    screen.blit(pacman_img,(pacman_obj[0],pacman_obj[1]))
    pygame.display.update()

