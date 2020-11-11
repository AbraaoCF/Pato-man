import pygame
from pygame.locals import *

#Initializing modules
pygame.init()
pygame.mixer.init()

#Getting images
background = pygame.image.load('imgs/background.png')
powerImg = pygame.image.load('imgs/corn.png')

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
        self.direct = LEFT
        self.last_direct = LEFT
        self.img = pygame.Surface((TS,TS))
        self.img.fill((255,255,255))

    def move(self):

        if self.direct == UP:
            self.pos = (self.pos[0],self.pos[1]-TS)
        if self.direct == RIGHT:
            self.pos = (self.pos[0]+TS,self.pos[1])
        if self.direct == DOWN:
            self.pos = (self.pos[0],self.pos[1]+TS)
        if self.direct == LEFT:
            self.pos=(self.pos[0]-TS,self.pos[1])
        
        if self.pos[1] == 17*TS:
            if self.pos[0] < 0:
                self.move_absolute(screen.get_width()-TS,self.pos[1])
            elif self.pos[0] >= screen.get_width():
                self.move_absolute(0,self.pos[1])
        
        if matriz[self.grid_pos()[0]][self.grid_pos()[1]] == 1:
            if self.direct == UP:
                self.pos = (self.pos[0], self.pos[1] + TS)
            if self.direct == RIGHT:
                self.pos = (self.pos[0] - TS, self.pos[1])
            if self.direct == DOWN:
                self.pos = (self.pos[0], self.pos[1] - TS)
            if self.direct == LEFT:
                self.pos = (self.pos[0] + TS, self.pos[1])
                
            if self.last_direct != self.direct:
                self.direct = self.last_direct
                self.move()
        
        self.last_direct = self.direct

    def move_absolute(self,x,y):
        self.pos=(x,y)

    def grid_pos(self):
        return (self.pos[1]//16,self.pos[0]//16)

class Score:

    def __init__(self):
        self.font=pygame.font.Font("fonts/emulogic.ttf",16) #loads the font file with letter size equal to 16 pixels

        self.score='00' #starting score
        self.high_score='00' #Starts as last high value if played before, need to implement whan we get there

        self.high_score_text=self.font.render(self.high_score,False,pygame.Color("white")) #makes starter high score text 
        self.score_text=self.font.render(self.score,False,pygame.Color("white")) #makes starter score text
        
    def display(self):
        screen.blit(self.font.render("high score",False,pygame.Color("white")),(144,0)) #display "high score" on screen
        screen.blit(self.score_text,(112-16*len(self.score),16)) #display current score on screen
        screen.blit(self.high_score_text,(272-16*len(self.high_score),16)) #display current high score on screen


    def add(self,num):
        self.score=str(int(self.score)+num) #updates current score
        if int(self.score)>int(self.high_score): #checks if we need new high score
            self.high_score=self.score #gets new high score value
            self.high_score_text=self.font.render(self.high_score,False,pygame.Color("white")) #makes new high score text
        self.score_text=self.font.render(self.score,False,pygame.Color("white")) #makes new score text
    
player = Player()
score=Score()

#Create coin
coinImg = pygame.Surface((4,4))
coinImg.fill((255,255,0))

#Screen
screen = pygame.display.set_mode((TS * 28, TS * 36))
pygame.display.set_caption("Pato-man")

#Clock Speed
clock = pygame.time.Clock()

#Inital screen appearence
screen.fill((0, 0, 0))
score.display()
screen.blit(background,(0,3*TS))
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
    
    if matriz[player.grid_pos()[0]][player.grid_pos()[1]] == 2:
        matriz[player.grid_pos()[0]][player.grid_pos()[1]] = 0
        score.add(10)
    elif matriz[player.grid_pos()[0]][player.grid_pos()[1]] == 3:
        matriz[player.grid_pos()[0]][player.grid_pos()[1]] = 0
        score.add(50)
    
    #Display objects on screen
    screen.fill((0, 0, 0))
    score.display()
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
