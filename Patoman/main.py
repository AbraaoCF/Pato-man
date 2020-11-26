import pygame
import os
from pygame.locals import *
import shelve
from Patoman import Matriz
from Patoman import menu
from Patoman import Ghost
power_song = False
main_dir = os.path.split(os.path.abspath(__file__))[0]
shelve_path=os.path.join(main_dir,"score.txt")

def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

def load_sound(name,volume):
   path=os.path.join(main_dir,"sounds",name)
   this_sound = pygame.mixer.Sound(path)
   this_sound.set_volume(volume)
   return this_sound

def play_music(name,volume):
   path=os.path.join(main_dir,"sounds",name)
   pygame.mixer.music.load(path)
   pygame.mixer.music.set_volume(volume)
   pygame.mixer.music.play(loops=-1)

def load_font(name,size):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,size)

def go_to_menu():
   running=False
   pygame.mixer.music.unload()
   pygame.mixer.pause()
   menu.run()

def game(volume,game_speed,diff):
    global power_song
    #Initializing modules
    pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    #Loads images
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
    arrow = load_img('arrow.png')

    #Loads the sounds
    eat1 = load_sound('pac_chomp_one.wav',volume)
    eat2 = load_sound('pac_chomp_two.wav',volume)
    death = load_sound('death.wav',volume)
    eat_ghost = load_sound('eat.wav',volume)

    #loads the fonts
    font=load_font("emulogic.ttf",16) 
    big_font=load_font("emulogic.ttf",32)

    #Stage 1 matrix. Holds information on active game state
    #State 0 --> Empty
    #State 1 --> Wall
    #State 2 --> Coin
    #State 3 --> Power
    matriz = Matriz.mat()

    #Directions
    UP    = 0
    LEFT  = 1
    DOWN  = 2
    RIGHT = 3

    #Tile Size (Define the number of pixels on each tile)
    TS = 8
    
    #Defining Ghosts
    Inky = 0
    Blinky = 1
    Clyde = 2
    Pinky = 3
    
    #Defining Ghosts' modes
    SCATTER = 0
    CHASE = 1
    EATEN = 2
    FRIGHTENED = 3
    LEAVE = 4
    WAITING = 5

    phantom = [Ghost.Ghost(0), Ghost.Ghost(1), Ghost.Ghost(2), Ghost.Ghost(3)]

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
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
            self.eaten_phantom = 0
            
        def set_xy(self):
            self.rect.x = self.pos[0]-4
            self.rect.y = self.pos[1]-8
        
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

            if matriz[self.grid_pos()[0]][self.grid_pos()[1]] == 1 or matriz[self.grid_pos()[0]][self.grid_pos()[1]] == 4:
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
            self.set_xy()

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
            self.rect = self.imgs[self.img_index].get_rect()
            self.set_xy()
            self.img_index=0
        
        def collision(self):

            phantom_list = pygame.sprite.Group()
            
            phantom_list.add(phantom[Inky  ])
            phantom_list.add(phantom[Blinky])
            phantom_list.add(phantom[Clyde ])
            phantom_list.add(phantom[Pinky ])
            
            phantom_player_collision = pygame.sprite.spritecollide(player, phantom_list, True)
            
            for ghost in phantom_player_collision:
                
                if (ghost.mode == EATEN):
                    continue
                if (ghost.mode == FRIGHTENED):
                    
                    phantom[ghost.ghost].mode = EATEN
                    eat_ghost.play()
                    pygame.time.wait(200)
                    phantom[ghost.ghost].box = False
                    score.add(200 * (2 ** self.eaten_phantom))
                    self.eaten_phantom += 1
                else:
                    pygame.mixer.music.unload()
                    death.play()
                    pygame.time.wait(2000)
                    go_to_menu()
    
    class Score:

        def __init__(self):
            
            self.score='00' #starting score
            d = shelve.open(shelve_path)#open high score memory
            self.high_score='00'
            if diff == 'easy' and 'score' in d:
                self.high_score=d['score'] #Starts as last high value if played before (modo normal)
            elif diff == 'hard' and 'score_gamer' in d:
                self.high_score=d['score_gamer'] #Starts as last high value if played before (modo gamer)

            d.close() #close high score memory
            self.high_score_text=font.render(self.high_score,False,pygame.Color("white")) #makes starter high score text 
            self.score_text=font.render(self.score,False,pygame.Color("white")) #makes starter score text

        def display(self):
            screen.blit(font.render("high score",False,pygame.Color("white")),(144,0)) #display "high score" on screen
            screen.blit(self.score_text,(112-16*len(self.score),16)) #display current score on screen
            screen.blit(self.high_score_text,(272-16*len(self.high_score),16)) #display current high score on screen


        def add(self,num):
            self.score=str(int(self.score)+num) #updates current score
            if int(self.score)>int(self.high_score): #checks if we need new high score
                d = shelve.open(shelve_path) #open high score memory
                if diff == 'easy':
                    d['score'] = self.score #update high score memory (modo normal)
                if diff == 'hard':
                    d['score_gamer'] = self.score #update high score memory (modo gamer)

                d.close() #close high score memory
                self.high_score=self.score #gets new high score value
                self.high_score_text=font.render(self.high_score,False,pygame.Color("white")) #makes new high score text
            self.score_text=font.render(self.score,False,pygame.Color("white")) #makes new score text

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
      cursor_index=0
      pygame.mixer.music.pause()
      pygame.mixer.pause()
      pause_screen=pygame.Surface((TS*56,TS*72))
      pause_screen.set_alpha(100)
      positions=[(TS*9,TS*28+4),(TS*1,TS*34+4)]
      while not running:

         clock.tick(60)
         for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
               pygame.quit()

            #Directions keys
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running=True
                   pygame.mixer.music.unpause()
                   pygame.mixer.unpause()

                if event.key == K_RETURN:

                   if cursor_index==0:
                      running=True
                      pygame.mixer.music.unpause()
                      pygame.mixer.unpause()
                      pygame.mixer.music.unpause()
                   else:
                      go_to_menu()
                if event.key == K_UP:
                   cursor_index+=1
                   if cursor_index==2:
                      cursor_index=0
                   
                if event.key == K_DOWN:
                   cursor_index-=1
                   if cursor_index==-1:
                      cursor_index=1

         screen.fill((0, 0, 0))
         score.display()
         screen.blit(background,(0, 6*TS))
         player.display()  
         #Display coins and powers on screen
         all_sprites_list.draw(screen)
         screen.blit(pause_screen,(0,0))
         screen.blit(big_font.render("PAUSED",False,pygame.Color("White")),(TS*16,TS*16))
         screen.blit(big_font.render("continue", False, pygame.Color('White')),(TS*12,TS*28))
         screen.blit(big_font.render("back to menu", False, pygame.Color('White')),(TS*4,TS*34))
         screen.blit(arrow,positions[cursor_index])

         pygame.display.update()

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
    screen.blit(font.render("ready!",False,pygame.Color("yellow")),(TS*22,TS*40))
    screen.blit(font.render("player one",False,pygame.Color("cyan")),(TS*18,TS*28))
    pygame.display.update()

    #Plays the beginning sound
    play_music('begin.wav',volume)
    pygame.time.wait(2150)
    
    #Set sprite position right
    Ajuste = 6
    
    #initial screen appearence 2
    screen.blit(background,(0,6*TS))
    all_sprites_list.draw(screen) #Print the sprites of the group of all sprites
    screen.blit(phantom[Blinky].img, (phantom[Blinky].pos[0] - Ajuste, phantom[Blinky].pos[1] - Ajuste))
    screen.blit(phantom[Inky  ].img, (phantom[Inky  ].pos[0] - Ajuste, phantom[Inky  ].pos[1] - Ajuste))
    screen.blit(phantom[Clyde ].img, (phantom[Clyde ].pos[0] - Ajuste, phantom[Clyde ].pos[1] - Ajuste))
    screen.blit(phantom[Pinky ].img, (phantom[Pinky ].pos[0] - Ajuste, phantom[Pinky ].pos[1] - Ajuste))
    screen.blit(font.render("ready!",False,pygame.Color("yellow")),(TS*22,TS*40))
    player.display()
    pygame.display.update()

    #Waits until sound is over so game can start
    pygame.time.wait(2150)
    play_music('music1.wav',volume)
    level_music = 'music1.wav'
    now_music = 'music1.wav'
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

        #changes pato-man's mouth animation
        player.aberto=not player.aberto


        #If after .move() memory_direction failed or not
        if player.change == 2:
            player.change = 1
        else:
            player.change = 0

        #pato-man eats a normal pellet
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

        #Pato-man eats a power pellet
        elif matriz[player.grid_pos()[0]][player.grid_pos()[1]] == 3:
            
            player.eaten_phantom=0

            #update ghots' state
            if (phantom[Blinky].mode != EATEN):
                if(phantom[Blinky].mode == LEAVE):
                    phantom[Blinky].frightened = True
                else:
                    if(phantom[Blinky].mode != FRIGHTENED):
                        phantom[Blinky].change_direct()
                    phantom[Blinky].mode = FRIGHTENED
                phantom[Blinky].moviments = 0
            if (phantom[Inky  ].mode != EATEN):
                if(phantom[Inky  ].mode == WAITING or phantom[Inky  ].mode == LEAVE):
                    phantom[Inky  ].frightened = True
                else:
                    if(phantom[Inky  ].mode != FRIGHTENED):
                        phantom[Inky  ].change_direct()
                    phantom[Inky  ].mode = FRIGHTENED
                phantom[Inky  ].moviments = 0
            if (phantom[Clyde ].mode != EATEN):
                if(phantom[Clyde  ].mode == WAITING or phantom[Clyde  ].mode == LEAVE):
                    phantom[Clyde  ].frightened = True
                else:
                    if(phantom[Clyde ].mode != FRIGHTENED):
                        phantom[Clyde ].change_direct()
                    phantom[Clyde ].mode = FRIGHTENED
                phantom[Clyde ].moviments = 0
            if (phantom[Pinky ].mode != EATEN):
                if(phantom[Pinky ].mode == LEAVE):
                    phantom[Pinky ].frightened = True
                else:
                    if(phantom[Pinky ].mode != FRIGHTENED):
                        phantom[Pinky ].change_direct()
                    phantom[Pinky ].mode = FRIGHTENED
                phantom[Pinky ].moviments = 0

            if(phantom[Blinky].mode == FRIGHTENED or phantom[Inky  ].mode == FRIGHTENED or phantom[Clyde ].mode == FRIGHTENED or phantom[Pinky ].mode == FRIGHTENED):
                power_on = True
            if(phantom[Blinky].frightened or phantom[Inky  ].frightened or phantom[Clyde ].frightened or phantom[Pinky ].frightened):
                power_on = True
            
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
            
        #music handler
        #------------------------------------------
        if (phantom[Blinky].mode == FRIGHTENED or phantom[Inky  ].mode == FRIGHTENED or phantom[Clyde ].mode == FRIGHTENED or phantom[Pinky ].mode == FRIGHTENED):
            if now_music!='power.wav' and now_music!='eyes.wav':
               now_music='power.wav'
               play_music('power.wav',volume)

        if (phantom[Blinky].mode == EATEN or phantom[Inky  ].mode == EATEN or phantom[Clyde ].mode == EATEN or phantom[Pinky ].mode == EATEN):
            if now_music!='eyes.wav':
               now_music='eyes.wav'
               play_music('eyes.wav',volume)
        elif now_music=='eyes.wav' and not (phantom[Blinky].mode == EATEN or phantom[Inky  ].mode == EATEN or phantom[Clyde ].mode == EATEN or phantom[Pinky ].mode == EATEN):
           now_music=''

        if not (phantom[Blinky].mode == FRIGHTENED or phantom[Inky  ].mode == FRIGHTENED or phantom[Clyde ].mode == FRIGHTENED or phantom[Pinky ].mode == FRIGHTENED) and not (phantom[Blinky].mode == EATEN or phantom[Inky  ].mode == EATEN or phantom[Clyde ].mode == EATEN or phantom[Pinky ].mode == EATEN or phantom[Blinky].frightened or phantom[Inky  ].frightened or phantom[Clyde ].frightened or phantom[Pinky ].frightened):
            if now_music!=level_music:
               now_music=level_music
               play_music(level_music,volume)

        if len(power_list)+len(coins_list)==144:
           level_music = 'music2.wav'

        if len(power_list)+len(coins_list)==83:
           level_music = 'music3.wav'

        if len(power_list)+len(coins_list)==27:
           level_music = 'music4.wav'
        #------------------------------------------

        #goes back to menu when level is finished
        if len(power_list)==0 and len(coins_list)==0:
           go_to_menu()

        #Display objects on screen
        screen.fill((0, 0, 0))
        score.display()
        screen.blit(background,(0, 6*TS))
        player.display()  
        
        phantom[Blinky].move(player.pos[1] // TS, player.pos[0] // TS, player.direct, 0, 0, 0)
        phantom[Inky  ].move(player.pos[1] // TS, player.pos[0] // TS, player.direct, phantom[Blinky].pos[1] // TS, phantom[Blinky].pos[0] // TS, len(power_list) + len(coins_list))
        phantom[Clyde ].move(player.pos[1] // TS, player.pos[0] // TS, player.direct, 0, 0, 0)
        phantom[Pinky ].move(player.pos[1] // TS, player.pos[0] // TS, player.direct, 0, 0, 0)
        
        player.collision()
        
        #Display coins and powers on screen
        all_sprites_list.draw(screen)
        
        screen.blit(phantom[Blinky].img, (phantom[Blinky].pos[0]-Ajuste, phantom[Blinky].pos[1]-Ajuste))
        screen.blit(phantom[Inky  ].img, (phantom[Inky  ].pos[0]-Ajuste, phantom[Inky  ].pos[1]-Ajuste))
        screen.blit(phantom[Clyde ].img, (phantom[Clyde ].pos[0]-Ajuste, phantom[Clyde ].pos[1]-Ajuste))
        screen.blit(phantom[Pinky ].img, (phantom[Pinky ].pos[0]-Ajuste, phantom[Pinky ].pos[1]-Ajuste))

        pygame.display.update()

if __name__=='__main__':
    game(volume=0.5,game_speed=15,diff="easy")
