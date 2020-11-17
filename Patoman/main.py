import pygame
import os
from pygame.locals import *

from Patoman import Matriz

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

def load_sound(name,volume):
   path=os.path.join(main_dir,"sounds",name)
   this_sound = pygame.mixer.Sound(path)
   this_sound.set_volume(volume)
   return this_sound

def load_font(name):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,16)

def game(volume,game_speed,diff):

    #Initializing modules
    pygame.init()
    pygame.mixer.init()

    #Getting images
    background = load_img('background.png')
    power_img = load_img('corn.png')
    coin_img = load_img('bit.png')
    patoFC = load_img('patoFC.png')
    patoFD = load_img('patoFD.png')
    patoFB = load_img('patoFB.png')
    patoFE = load_img('patoFE.png')
    patoAC = load_img('patoAC.png')
    patoAD = load_img('patoAD.png')
    patoAB = load_img('patoAB.png')
    patoAE = load_img('patoAE.png')

    #Creating the sounds
    eat1 = load_sound('pac_chomp_one.wav',volume)
    eat2 = load_sound('pac_chomp_two.wav',volume)
    music1 = load_sound('music1.wav',volume)
    music2 = load_sound('music2.wav',volume)
    music3 = load_sound('music3.wav',volume)
    music4 = load_sound('music4.wav',volume)
    power = load_sound('power.wav',volume)
    begin = load_sound('begin.wav',volume)
    
    #Stage 1 matrix. Holds information on active game state
    #State 0 --> Empty
    #State 1 --> Wall
    #State 2 --> Coin
    #State 3 --> Power
    matriz = Matriz.mat()

    #Directions
    UP    = 0
    RIGHT = 1
    DOWN  = 2
    LEFT  = 3

    #Tile Size (Define the number of pixels on each tile)
    TS = 8

    class Player(pygame.sprite.Sprite):

        def __init__(self):
            self.pos = (27*TS,52*TS)
            self.direct = LEFT
            self.last_direct = LEFT
            self.memory_direct = LEFT
            self.change = 0
            self.img_index=0
            self.imgs = [patoFC,patoFD,patoFB,patoFE,patoAC,patoAD,patoAB,patoAE]
            self.image = patoFC
            self.rect = self.image.get_rect()
            self.aberto=False

        def move(self):

            #Try (only one time) to do the memory direction
            if self.change == 1:
                self.direct = self.memory_direct

            if self.direct == UP:
                self.pos = (self.pos[0],self.pos[1]-TS)
            if self.direct == RIGHT:
                self.pos = (self.pos[0]+TS,self.pos[1])
            if self.direct == DOWN:
                self.pos = (self.pos[0],self.pos[1]+TS)
            if self.direct == LEFT:
                self.pos=(self.pos[0]-TS,self.pos[1])

            if self.pos[1] == 34*TS:
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

                    #If direction is invalid, memory_direction save it
                    self.memory_direct = self.direct
                    self.change += 1

                    self.direct = self.last_direct
                    self.move()

            self.last_direct = self.direct

        def move_absolute(self,x,y):
            self.pos=(x,y)

        def grid_pos(self):
            return (self.pos[1]//TS,self.pos[0]//TS)

        def display(self):
            if self.aberto:
                self.img_index+=4
            if self.direct==RIGHT:
                self.img_index+=1
            elif self.direct==DOWN:
                self.img_index+=2
            elif self.direct==LEFT:
                self.img_index+=3
            screen.blit(self.imgs[self.img_index],(self.pos[0]-4,self.pos[1]-8))
            self.img_index=0
    
    class Score:

        def __init__(self):
            self.font=load_font("emulogic.ttf") #loads the font file with letter size equal to 16 pixels

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

    class Coins(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = coin_img
            self.rect = self.image.get_rect()


    class Power(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = power_img
            self.rect = self.image.get_rect()
            
    def pause_game():
      running=False
      pygame.mixer.pause()
      while not running:

         clock.tick(game_speed)
         for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
             pygame.quit()

            #Directions keys
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running=True
                   pygame.mixer.unpause()
           
    player = Player()
    score = Score()

    #Create the groups of sprites
    all_sprites_list = pygame.sprite.Group() 
    coins_list = pygame.sprite.Group()
    power_list = pygame.sprite.Group()

    #Create the sprites of coins and powers and put them in the respective groups
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            coins = Coins()
            power = Power()

            if (matriz[i][j] == 2):
                coins.rect.x = j * TS
                coins.rect.y = i * TS
                coins_list.add(coins)
                all_sprites_list.add(coins)

            if (matriz[i][j] == 3):
                power.rect.x = j * TS
                power.rect.y = i * TS
                power_list.add(power)
                all_sprites_list.add(power)

    #Screen
    screen = pygame.display.set_mode((TS * 56, TS * 72))
    pygame.display.set_caption("Pato-man")
    #Clock Speed
    clock = pygame.time.Clock()

    #Inital screen appearence
    screen.fill((0, 0, 0))
    score.display()
    screen.blit(background,(0,6*TS))
    all_sprites_list.draw(screen) #Print the sprites of the group of all sprites
    
    screen.blit(score.font.render("ready!",False,pygame.Color("yellow")),(TS*22,TS*40))
    screen.blit(score.font.render("player one",False,pygame.Color("cyan")),(TS*18,TS*28))
    
    pygame.display.update()

    #Plays the beginning sound
    begin.play()

    pygame.time.wait(2150)
    screen.blit(background,(0,6*TS))
    all_sprites_list.draw(screen) #Print the sprites of the group of all sprites
    
    screen.blit(score.font.render("ready!",False,pygame.Color("yellow")),(TS*22,TS*40))
  
    player.display() #display player
       
    pygame.display.update()
    #Waits until sound is over so game can start
    pygame.time.wait(2150)
    music1.play(loops=-1)

    #counter to change chomp sound
    counter = True

    running = True
    while running:
        clock.tick(game_speed)
        for event in pygame.event.get():

            #Quit game
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            #Directions keys
            if event.type == KEYDOWN:
                player.change = 0 #If key is used, memory_direction has to update
                if event.key == K_UP:
                    player.direct = UP
                if event.key == K_DOWN:
                    player.direct = DOWN
                if event.key == K_LEFT:
                    player.direct = LEFT
                if event.key == K_RIGHT:
                    player.direct = RIGHT
                if event.key == K_ESCAPE:
                   pause_game()

        #Handles player movement
        player.move()
        player.aberto=not player.aberto

        #If after .move() memory_direction failed or not
        if player.change == 2:
            player.change = 1
        else:
            player.change = 0

        if matriz[player.grid_pos()[0]][player.grid_pos()[1]] == 2:

            for coins in coins_list: #Search the atual coins in coins_list
                if coins.rect.x == player.grid_pos()[1] * TS and coins.rect.y == player.grid_pos()[0] * TS:
                    coins.kill() #Remove from all groups
                    break

            matriz[player.grid_pos()[0]][player.grid_pos()[1]] = 0
            score.add(10)

            #change chomp sound
            if counter:
                eat1.play()
            else:
                eat2.play()
            counter = not counter

        elif matriz[player.grid_pos()[0]][player.grid_pos()[1]] == 3:

            for power in power_list: #Search the atual power in power_list
                if power.rect.x == player.grid_pos()[1] * TS and power.rect.y == player.grid_pos()[0] * TS:
                    power.kill() #Remove from all groups
                    break

            matriz[player.grid_pos()[0]][player.grid_pos()[1]] = 0
            score.add(50)

            #change chomp sound
            if counter:
                eat1.play()
            else:
                eat2.play()
            counter = not counter

        if len(power_list)+len(coins_list)==184 and music2.get_num_channels()==0:
           music1.stop()
           music2.play(loops=-1)
        if len(power_list)+len(coins_list)==123 and music3.get_num_channels()==0:
           music2.stop()
           music3.play(loops=-1)
        if len(power_list)+len(coins_list)==61 and music4.get_num_channels()==0:
           music3.stop()
           music4.play(loops=-1)
        
        if len(power_list)==0 and len(coins_list)==0:
            running=False
            pygame.quit()


        #Display objects on screen
        screen.fill((0, 0, 0))
        score.display()
        screen.blit(background,(0, 6*TS))
        player.display()  

        #Display coins and powers on screen
        all_sprites_list.draw(screen)

        pygame.display.update()

if __name__=='__main__':
    game(volume=0.5,game_speed=15,diff="easy")
