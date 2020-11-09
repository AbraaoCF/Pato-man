import pygame
from pygame.locals import *

#Initializing modules
pygame.init()
pygame.mixer.init()

#Getting images
background=pygame.image.load('imgs/background.png')

#Creating the sounds
begin=pygame.mixer.Sound('sounds/begin.wav')

#Stage 1 matrix. Holds information on active game state
matriz = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

#Directions
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

#Tile Size (Define the number of pixels on each tile)
TS = 16

class Player:

    def __init__(self):
        self.pos=(14*TS,26*TS)
        self.direct=LEFT
        self.img=pygame.Surface((TS,TS))
        self.img.fill((255,255,0))

    def move(self):
        if self.direct == UP:
            self.pos=(self.pos[0],self.pos[1]-TS)
        if self.direct == RIGHT:
            self.pos=(self.pos[0]+TS,self.pos[1])
        if self.direct == DOWN:
            self.pos=(self.pos[0],self.pos[1]+TS)
        if self.direct == LEFT:
            self.pos=(self.pos[0]-TS,self.pos[1])

    def move_absolute(self,x,y):
        self.pos=(x,y)

player = Player()

#Tile Size (Define the number of pixels on each tile)
TS = 16

#Screen
screen = pygame.display.set_mode((TS * 28, TS * 36))
pygame.display.set_caption("Pato-man")


last_direction = LEFT

#Clock Speed
clock = pygame.time.Clock()

#Inital screen appearence
screen.fill((0, 0, 0))
screen.blit(background,(0,3*TS));
screen.blit(player.img,player.pos)
pygame.display.update()

#Plays the beginning sound
begin.play()
#waits until sound is over so game can start
pygame.time.wait(4300);

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
  
        # Quit game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #Directions keys
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.direct = UP
            if event.key == K_DOWN:
                player.direct = DOWN
            if event.key == K_LEFT:
                player.direct = LEFT
            if event.key == K_RIGHT:
                player.direct = RIGHT

    #Handles player movement
    player.move()

    if player.pos[1] == TS*17:
        if player.pos[0] < 0:
            player.pos = (screen.get_width() - TS, player.pos[1])
        elif player.pos[0] >= screen.get_width():
            player.pos = (0 - TS, player.pos[1])

    #Makes Pac-man stop on walls
    if (matriz[player.pos[1] // TS][player.pos[0] // TS] == 1):
        if player.direct == UP:
                player.pos = (player.pos[0], player.pos[1] + TS)
        if player.direct == RIGHT:
                player.pos = (player.pos[0] - TS, player.pos[1])
        if player.direct == DOWN:
                player.pos = (player.pos[0], player.pos[1] - TS)
        if player.direct == LEFT:
                player.pos = (player.pos[0] + TS, player.pos[1])
	
      # Not change direction on walls
        if last_direction != player.direct:
            player.direct = last_direction
            player.move()

     # Corners
        if (matriz[player.pos[1] // TS][player.pos[0] // TS] == 1):
            if player.direct == UP:
                player.pos = (player.pos[0], player.pos[1] + TS)
            if player.direct == RIGHT:
                player.pos = (player.pos[0] - TS, player.pos[1])
            if player.direct == DOWN:
                player.pos = (player.pos[0], player.pos[1] - TS)
            if player.direct == LEFT:
                player.pos = (player.pos[0] + TS, player.pos[1])
    last_direction = player.direct
  
    #Display objects on screen
    screen.fill((0, 0, 0))
    screen.blit(background,(0,3*TS))
    screen.blit(player.img,player.pos)
    pygame.display.update()
