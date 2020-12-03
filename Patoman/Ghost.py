import random
import os
import pygame
from pygame.locals import *
import time
from Patoman import Matriz


main_dir = os.path.split(os.path.abspath(__file__))[0]
def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

matriz = Matriz.mat();

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
NONE = 4

Inky = 0
Blinky = 1
Clyde = 2
Pinky = 3

SCATTER = 0
CHASE = 1
EATEN = 2
FRIGHTENED = 3
LEAVE = 4
WAITING = 5

TS = 1
limit = len(matriz[0])

imgs =  [
[
[[load_img('InkyUp1.png'  ), load_img('InkyUp2.png'  )], [load_img('InkyLeft1.png'  ), load_img('InkyLeft2.png'  )], [load_img('InkyDown1.png'  ), load_img('InkyDown2.png'  )], [load_img('InkyRight1.png'  ), load_img('InkyRight2.png'  )]],
[[load_img('BlinkyUp1.png'), load_img('BlinkyUp2.png')], [load_img('BlinkyLeft1.png'), load_img('BlinkyLeft2.png')], [load_img('BlinkyDown1.png'), load_img('BlinkyDown2.png')], [load_img('BlinkyRight1.png'), load_img('BlinkyRight2.png')]],
[[load_img('ClydeUp1.png' ), load_img('ClydeUp2.png' )], [load_img('ClydeLeft1.png' ), load_img('ClydeLeft2.png' )], [load_img('ClydeDown1.png' ), load_img('ClydeDown2.png' )], [load_img('ClydeRight1.png' ), load_img('ClydeRight2.png' )]],
[[load_img('PinkyUp1.png' ), load_img('PinkyUp2.png' )], [load_img('PinkyLeft1.png' ), load_img('PinkyLeft2.png' )], [load_img('PinkyDown1.png' ), load_img('PinkyDown2.png' )], [load_img('PinkyRight1.png' ), load_img('PinkyRight2.png' )]],
],
[
[[load_img('InkyUp1.png'  ), load_img('InkyUp2.png'  )], [load_img('InkyLeft1.png'  ), load_img('InkyLeft2.png'  )], [load_img('InkyDown1.png'  ), load_img('InkyDown2.png'  )], [load_img('InkyRight1.png'  ), load_img('InkyRight2.png'  )]],
[[load_img('BlinkyUp1.png'), load_img('BlinkyUp2.png')], [load_img('BlinkyLeft1.png'), load_img('BlinkyLeft2.png')], [load_img('BlinkyDown1.png'), load_img('BlinkyDown2.png')], [load_img('BlinkyRight1.png'), load_img('BlinkyRight2.png')]],
[[load_img('ClydeUp1.png' ), load_img('ClydeUp2.png' )], [load_img('ClydeLeft1.png' ), load_img('ClydeLeft2.png' )], [load_img('ClydeDown1.png' ), load_img('ClydeDown2.png' )], [load_img('ClydeRight1.png' ), load_img('ClydeRight2.png' )]],
[[load_img('PinkyUp1.png' ), load_img('PinkyUp2.png' )], [load_img('PinkyLeft1.png' ), load_img('PinkyLeft2.png' )], [load_img('PinkyDown1.png' ), load_img('PinkyDown2.png' )], [load_img('PinkyRight1.png' ), load_img('PinkyRight2.png' )]],
],
[
[[load_img('EatenUp.png'), load_img('EatenUp.png')], [load_img('EatenLeft.png'), load_img('EatenLeft.png')], [load_img('EatenDown.png'), load_img('EatenDown.png')], [load_img('EatenRight.png'), load_img('EatenRight.png')]],
[[load_img('EatenUp.png'), load_img('EatenUp.png')], [load_img('EatenLeft.png'), load_img('EatenLeft.png')], [load_img('EatenDown.png'), load_img('EatenDown.png')], [load_img('EatenRight.png'), load_img('EatenRight.png')]],
[[load_img('EatenUp.png'), load_img('EatenUp.png')], [load_img('EatenLeft.png'), load_img('EatenLeft.png')], [load_img('EatenDown.png'), load_img('EatenDown.png')], [load_img('EatenRight.png'), load_img('EatenRight.png')]],
[[load_img('EatenUp.png'), load_img('EatenUp.png')], [load_img('EatenLeft.png'), load_img('EatenLeft.png')], [load_img('EatenDown.png'), load_img('EatenDown.png')], [load_img('EatenRight.png'), load_img('EatenRight.png')]],
],
[
[[load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')]],
[[load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')]],
[[load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')]],
[[load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')], [load_img('Frightened1.png'), load_img('Frightened2.png')]],
],
[
[[load_img('InkyUp1.png'  ), load_img('InkyUp2.png'  )], [load_img('InkyLeft1.png'  ), load_img('InkyLeft2.png'  )], [load_img('InkyDown1.png'  ), load_img('InkyDown2.png'  )], [load_img('InkyRight1.png'  ), load_img('InkyRight2.png'  )]],
[[load_img('BlinkyUp1.png'), load_img('BlinkyUp2.png')], [load_img('BlinkyLeft1.png'), load_img('BlinkyLeft2.png')], [load_img('BlinkyDown1.png'), load_img('BlinkyDown2.png')], [load_img('BlinkyRight1.png'), load_img('BlinkyRight2.png')]],
[[load_img('ClydeUp1.png' ), load_img('ClydeUp2.png' )], [load_img('ClydeLeft1.png' ), load_img('ClydeLeft2.png' )], [load_img('ClydeDown1.png' ), load_img('ClydeDown2.png' )], [load_img('ClydeRight1.png' ), load_img('ClydeRight2.png' )]],
[[load_img('PinkyUp1.png' ), load_img('PinkyUp2.png' )], [load_img('PinkyLeft1.png' ), load_img('PinkyLeft2.png' )], [load_img('PinkyDown1.png' ), load_img('PinkyDown2.png' )], [load_img('PinkyRight1.png' ), load_img('PinkyRight2.png' )]],
]
		]
		
frightened_img = [
[load_img('Frightened1.png'), load_img('Frightened2.png')],
[load_img('FrightenedBlink1.png'), load_img('FrightenedBlink2.png')]
				 ]

Blinky_img = pygame.Surface((16,16))
Blinky_img.fill((255,0,0))

Inky_img = pygame.Surface((16,16))
Inky_img.fill((19,249,226))

Clyde_img = pygame.Surface((16,16))
Clyde_img.fill((209,239,13))

Pinky_img = pygame.Surface((16,16))
Pinky_img.fill((218,15,245))

Ajuste = 6

class Ghost(pygame.sprite.Sprite):
	
   def __init__(self, type_ghost):
      self.ghost = type_ghost

      if(self.ghost == Inky):
         self.pos = (184, 280)
      if(self.ghost == Blinky):
         self.pos = (216, 224)
      if(self.ghost == Clyde):
         self.pos = (248, 280)
      if(self.ghost == Pinky):
         self.pos = (216 * TS, 280)

      self.mode = LEAVE
 
      pygame.sprite.Sprite.__init__(self)
      self.direct = DOWN
      self.change = 0
      self.img = imgs[self.mode][self.ghost][self.direct][self.change]
      self.rect = self.img.get_rect()
      self.rect.height = 16
      self.rect.width = 16
      self.rect.x = self.pos[0]
      self.rect.y = self.pos[1]
      self.time = 0
      self.timer = time.time()
      self.normal_speed=0
      self.slow_speed=0
      self.speed=0

      if(self.ghost == Pinky):
         self.mode = LEAVE
      if(self.ghost == Blinky):
         self.mode = SCATTER
      if(self.ghost == Clyde):
         self.mode = WAITING
         self.waiting_moviments = -30
         self.up = True
      if(self.ghost == Inky):
         self.mode = WAITING
         self.waiting_moviments = 0
         self.up = True

      self.frightened = False

      self.box = False

      self.moviments = 0
	
   def dis(self, x, y):
      return (self.target[0] - x) ** 2 + (self.target[1] - y) ** 2
  
   def change_direct(self):
      if(self.direct == UP):
         self.direct = DOWN
      elif(self.direct == DOWN):
         self.direct = UP
      elif(self.direct == RIGHT):
         self.direct = LEFT
      elif(self.direct == LEFT):
         self.direct = RIGHT
  
   def set_image(self):
      real_mode = self.mode
          
      if(self.mode == WAITING):
         if(self.frightened):
            self.mode = FRIGHTENED
         else:
            self.mode = SCATTER
      if(self.mode == LEAVE):
         if(self.frightened):
            self.mode = FRIGHTENED
       
      if(self.mode == FRIGHTENED and time.time() - self.timer >= 10):
         self.img = frightened_img[self.change][self.change]
      else:
         self.img = imgs[self.mode][self.ghost][self.direct][self.change]
          
      self.rect.x = self.pos[0]
      self.rect.y = self.pos[1]
          
      self.mode = real_mode
   
   def reset_time(self):
      self.timer = time.time()
   
   def move(self, x, y, direct, redx, redy, coins_left):
      possible_moviments = []
        
      self.change = (self.change + 1) % 2
          
      if(self.mode == SCATTER):
         self.speed=self.normal_speed
         if(self.ghost == Inky):
            self.target = (568, 440)
         if(self.ghost == Blinky):
            self.target = (-8, 408)
         if(self.ghost == Clyde):
            self.target = (568, 0)
         if(self.ghost == Pinky):
            self.target = (-8, 32)
            
         #Find possible Moviments for Ink
         if(self.direct != LEFT and matriz[self.pos[1]][(self.pos[0] + 1) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] + 1) % limit), RIGHT, self.pos[1], (self.pos[0] + 1) % limit])
         if(self.direct != RIGHT and matriz[self.pos[1]][(self.pos[0] - 1 + limit) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] - 1 + limit) % limit), LEFT, self.pos[1], (self.pos[0] - 1 + limit) % limit])
         if(self.direct != UP and matriz[self.pos[1] + 1][self.pos[0]] != 1 and matriz[self.pos[1] + 1][self.pos[0]] != 4):
            possible_moviments.append([self.dis(self.pos[1] + 1, self.pos[0]), DOWN, self.pos[1] + 1, self.pos[0]])
         if(self.direct != DOWN and matriz[self.pos[1] - 1][self.pos[0]] != 1):
            can = True
                        
            if((self.pos[1] // TS - 1 == 223 or self.pos[1] // TS - 1 == 415) and (self.pos[0] // TS == 192 or self.pos[0] // TS == 240)):
               can = False
            if(can):
               possible_moviments.append([self.dis(self.pos[1] - 1, self.pos[0]), UP, self.pos[1] - 1, self.pos[0]])
            
         #Calculate better moviment
         possible_moviments.sort()
                  
         self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
         self.direct = possible_moviments[0][1]
                  
         if(time.time() - self.timer >= 8):
            self.mode = CHASE
            self.change_direct()
            self.reset_time()
      elif(self.mode == FRIGHTENED):
         self.speed=self.slow_speed
            
         #Find possible Moviments
         if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % limit] != 1):
            possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS + 1) % limit, RIGHT])
         if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
            possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS - 1 + limit) % limit, LEFT])
         if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1 and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 4):
            possible_moviments.append([self.pos[1] // TS + 1, self.pos[0] // TS, DOWN])
         if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
            can = True
                          
            if((self.pos[1] // TS - 1 == 223 or self.pos[1] // TS - 1 == 415) and (self.pos[0] // TS == 192 or self.pos[0] // TS == 240)):
               can = False
            if(can):
               possible_moviments.append([self.pos[1] // TS - 1, self.pos[0] // TS, UP])
                  
         #Choose a random direction
         random_direct = random.choice(possible_moviments)
         self.pos = (random_direct[1] * TS, random_direct[0] * TS)
         self.direct = random_direct[2]
            
         if(time.time() - self.timer >= 12):
            if(coins_left < 80 and self.ghost == Blinky):
               self.mode = CHASE
            else:
               self.mode = SCATTER
                
               self.change_direct()
               self.reset_time()
      elif(self.mode == EATEN):
         self.speed=250
         if(self.box):
            if(self.ghost == Inky):
               self.target = (280, 184)
            if(self.ghost == Blinky):
               self.target = (280, 216)
            if(self.ghost == Clyde):
               self.target = (280, 248)
            if(self.ghost == Pinky):
               self.target = (280, 216)
         else: 
            self.target = (224, 216)
                  
         #Find possible Moviments for Ink
         if(self.direct != LEFT and matriz[self.pos[1]][(self.pos[0] + 1) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] + 1) % limit), RIGHT, self.pos[1], (self.pos[0] + 1) % limit])
         if(self.direct != RIGHT and matriz[self.pos[1]][(self.pos[0] - 1 + limit) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] - 1 + limit) % limit), LEFT, self.pos[1], (self.pos[0] - 1 + limit) % limit])
         if(self.direct != UP and matriz[self.pos[1] + 1][self.pos[0]] != 1):
            possible_moviments.append([self.dis(self.pos[1] + 1, self.pos[0]), DOWN, self.pos[1] + 1, self.pos[0]])
         if(self.direct != DOWN and matriz[self.pos[1] - 1][self.pos[0]] != 1):
            can = True
                        
            if((self.pos[1] // TS - 1 == 223 or self.pos[1] // TS - 1 == 415) and (self.pos[0] // TS == 192 or self.pos[0] // TS == 240)):
               can = False
            if(can):
               possible_moviments.append([self.dis(self.pos[1] - 1, self.pos[0]), UP, self.pos[1] - 1, self.pos[0]])
                  
         #Calculate better moviment
         possible_moviments.sort()
                  
         self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
         self.direct = possible_moviments[0][1]
            
         if(self.target[0] == (self.pos[1] // TS) and self.target[1] == (self.pos[0] // TS)):
                        
            if(self.box):
               self.mode = LEAVE
               self.change_direct()
            else:
               self.box = True
         
      elif(self.mode == CHASE):
         self.speed=self.normal_speed
         
         if(self.ghost == Inky):
            self.target = (x - (redx - x), y - (redy - y))
         if(self.ghost == Blinky):
            self.target = (x, y)
         if(self.ghost == Clyde):
            self.target = (x, y)
            
            if(self.dis(self.pos[1] // TS, self.pos[0] // TS) < 256):
               self.target = (568, 0)
         if(self.ghost == Pinky):
            if(direct == LEFT):
               self.target = (x, y - 64)
            if(direct == RIGHT):
               self.target = (x, y + 64)
            if(direct == DOWN):
               self.target = (x + 64, y)
            if(direct == UP):
               self.target = (x - 64, y - 64)
         #Find possible Moviments for Ink
         if(self.direct != LEFT and matriz[self.pos[1]][(self.pos[0] + 1) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] + 1) % limit), RIGHT, self.pos[1], (self.pos[0] + 1) % limit])
         if(self.direct != RIGHT and matriz[self.pos[1]][(self.pos[0] - 1 + limit) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1], (self.pos[0] - 1 + limit) % limit), LEFT, self.pos[1], (self.pos[0] - 1 + limit) % limit])
         if(self.direct != UP and matriz[self.pos[1] + 1][self.pos[0]] != 1 and matriz[self.pos[1] + 1][self.pos[0]] != 4):
            possible_moviments.append([self.dis(self.pos[1] + 1, self.pos[0]), DOWN, self.pos[1] + 1, self.pos[0]])
         if(self.direct != DOWN and matriz[self.pos[1] - 1][self.pos[0]] != 1):
            can = True
                        
            if((self.pos[1] // TS - 1 == 223 or self.pos[1] // TS - 1 == 415) and (self.pos[0] // TS == 192 or self.pos[0] // TS == 240)):
               can = False
            if(can):
               possible_moviments.append([self.dis(self.pos[1] - 1, self.pos[0]), UP, self.pos[1] - 1, self.pos[0]])
              
         #Calculate better moviment
         possible_moviments.sort()
              
         self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
         self.direct = possible_moviments[0][1]
              
         if(time.time() - self.timer >= 20):
            if(coins_left < 80 and self.ghost == Blinky):
               self.mode = CHASE
            else:
               self.mode = SCATTER
               self.change_direct()
            self.reset_time()
      elif(self.mode == LEAVE):
         self.speed=self.normal_speed
         self.target = (224, 216)
                  
         #Find possible Moviments
         if(matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % limit] != 1):
            possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % limit), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % limit])
         if(matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
            possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + limit) % limit), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + limit) % limit])
         if(matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
            possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
         if(matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
                     
            can = True
                          
            if((self.pos[1] // TS - 1 == 223 or self.pos[1] // TS - 1 == 415) and (self.pos[0] // TS == 192 or self.pos[0] // TS == 240)):
               can = False
            if(can):
               possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
                  
         #Calculate better moviment
         possible_moviments.sort()
                  
         self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
         self.direct = possible_moviments[0][1]
              
         if(self.frightened and time.time() - self.timer >= 20):
            self.frightened = False
              
         #Check if the ghost left the box
         if(self.target[0] == (self.pos[1] // TS) and self.target[1] == (self.pos[0] // TS)):
            if(self.frightened):
               self.mode = FRIGHTENED
               self.frightened = False
            elif(coins_left < 80 and self.ghost == Blinky):
               self.mode = CHASE
               self.reset_time()
            else:
               self.mode = SCATTER
               self.reset_time()
        
      elif(self.mode == WAITING):
         self.speed=self.normal_speed
         
         if(self.up):
            if(self.pos[1] // TS == 264):
               self.up = False
               self.pos = (self.pos[0], self.pos[1] + TS)
               self.direct = DOWN
            else:
               self.pos = (self.pos[0], self.pos[1] - TS)
         elif(not self.up):
            if(self.pos[1] // TS == 280):
               self.up = True
               self.waiting_moviments += 1
                                  
               if(self.waiting_moviments >= 10):
                  self.mode = LEAVE
               else:
                  self.pos = (self.pos[0], self.pos[1] - TS)
                  self.direct = UP
            else:
               self.pos = (self.pos[0], self.pos[1] + TS)
                
               if(time.time() - self.timer >= 12):
                  self.frightened = False
        
      self.set_image()
