import pygame
from pygame.locals import *

#Initializing modules
pygame.init()
pygame.mixer.init()

#Getting images
background = pygame.image.load('imgs/background.png')
powerImg = pygame.image.load('imgs/corn.png')

#Create coin
coinImg = pygame.Surface((4,4))
coinImg.fill((255,255,0))

#Creating the sounds
begin = pygame.mixer.Sound('sounds/begin.wav')

#Stage 1 matrix. Holds information on active game state
#State 0 --> Empty
#State 1 --> Wall
#State 2 --> Coin
#State 3 --> Power
matriz = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 3, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 1, 3, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
[1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
[1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
[1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
[1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]


#Directions
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

#Tile Size (Define the number of pixels on each tile)
TS = 16

class Player:

    def __init__(self):
        self.pos = (14*TS,26*TS)
        self.gridPosition = (26,14)
        self.direct = LEFT
        self.last_direction = LEFT
        self.img = pygame.Surface((TS,TS))
        self.img.fill((255,255,255))

    def move(self):

        if self.direct == UP:
            self.pos = (self.pos[0],self.pos[1]-TS)
            self.gridPosition = (self.gridPosition[0] - 1, self.gridPosition[1])
        if self.direct == RIGHT:
            self.pos = (self.pos[0]+TS,self.pos[1])
            self.gridPosition = (self.gridPosition[0], self.gridPosition[1] + 1)
        if self.direct == DOWN:
            self.pos = (self.pos[0],self.pos[1]+TS)
            self.gridPosition = (self.gridPosition[0] + 1, self.gridPosition[1])
        if self.direct == LEFT:
            self.pos=(self.pos[0]-TS,self.pos[1])
            self.gridPosition = (self.gridPosition[0], self.gridPosition[1] - 1)
        
        if self.pos[1] == TS*17:
            if self.pos[0] < 0:
                self.pos = (screen.get_width() - TS, self.pos[1])
                self.gridPosition = (14,27)
            elif self.pos[0] >= screen.get_width():
                self.pos = (0 - TS, self.pos[1])
                self.gridPosition = (14,0)
        
        if (matriz[self.pos[1] // TS][self.pos[0] // TS] == 1):
            if self.direct == UP:
                self.pos = (self.pos[0], self.pos[1] + TS)
            if self.direct == RIGHT:
                self.pos = (self.pos[0] - TS, self.pos[1])
            if self.direct == DOWN:
                self.pos = (self.pos[0], self.pos[1] - TS)
            if self.direct == LEFT:
                self.pos = (self.pos[0] + TS, self.pos[1])
                
            if self.last_direction != self.direct:
                self.direct = self.last_direction
                self.move()
        
        self.last_direction = self.direct

    def move_absolute(self,x,y):
        self.pos=(x,y)

player = Player()

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

#Display initial coins and powers on screen
for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
                screen.blit(coinImg, (j * TS + 6, i * TS + 6))
            if matriz[i][j] == 3:
                screen.blit(powerImg, (j * TS, i * TS))

pygame.display.update()

#Plays the beginning sound
begin.play()
#Waits until sound is over so game can start
pygame.time.wait(4300);

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
  
        #Quit game
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
    matriz[player.pos[1] // TS][player.pos[0] // TS] = 0


    #Display objects on screen
    screen.fill((0, 0, 0))
    screen.blit(background,(0, 3*TS))
    screen.blit(player.img,player.pos)  

    #Display coins and powers on screen
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
               screen.blit(coinImg, (j * TS + 6, i * TS + 6))
            if matriz[i][j] == 3:
                screen.blit(powerImg, (j * TS, i * TS))

    pygame.display.update()
