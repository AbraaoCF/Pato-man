import pygame
import os
from pygame.locals import *

from Patoman import main as level1

main_dir = os.path.split(os.path.abspath(__file__))[0]
def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

def load_sound(name):
   path=os.path.join(main_dir,"sounds",name)
   this_sound = pygame.mixer.Sound(path)
   this_sound.set_volume(0.3)
   return this_sound

def load_font(name,size):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,size)

def run():
   
   pygame.init() #initializing pygame
   pygame.mixer.init()

   # Limitations (inclusive) for menu options:
   #top: TS*32 bottom: TS*66
   #left: TS*4 right: TS*50

   #Directions
   UP    = 0
   RIGHT = 1
   DOWN  = 2
   LEFT  = 3
   STOP  = 4

   #loading resources
   patoFC = load_img('patoFC.png')
   patoFD = load_img('patoFD.png')
   patoFB = load_img('patoFB.png')
   patoFE = load_img('patoFE.png')
   patoAC = load_img('patoAC.png')
   patoAD = load_img('patoAD.png')
   patoAB = load_img('patoAB.png')
   patoAE = load_img('patoAE.png')

   font=load_font("emulogic.ttf",16)
   font_menu=load_font("emulogic.ttf",32)
   game_volume=50
   TS=8 #setting the size in pixels of a tile

   screen = pygame.display.set_mode((TS * 56, TS * 72)) #sets screen size
   pygame.display.set_caption("Pato-man") #sets screen title

   clock = pygame.time.Clock() #create clock object

   class Header():

       def __init__(self):
           self.title=load_img('patoman_logo.png'); #defines title image


       def display(self):
           #writes text to screen
           screen.blit(font.render("Controls: -Arrows to move",False,pygame.Color('White')),(16,160))
           screen.blit(font.render("          -Enter to select",False,pygame.Color('White')),(16,176))
           screen.blit(font.render("          -Esc to pause",False,pygame.Color('White')),(16,192))
           screen.blit(self.title,(81,64)) #shows title image

   class Main_Menu():

       def __init__(self):
           self.size = 3
           self.type = "Main Menu"
           self.positions=[(TS*15,TS*38+4),(TS*9,TS*44+4),(TS*12,TS*50+4),(TS*16,TS*56+4)]

       def display(self):
           screen.blit(font_menu.render("Start", False, pygame.Color('White')),(TS*19,TS*38))
           screen.blit(font_menu.render("Settings", False, pygame.Color('White')),(TS*13,TS*44))
           screen.blit(font_menu.render("Credits", False, pygame.Color('White')),(TS*15,TS*50))
           screen.blit(font_menu.render("Quit", False, pygame.Color('White')),(TS*20,TS*56))

   class Start_Menu():

       def __init__(self):
           self.size = 2
           self.type = "Start Menu"
           self.positions = [(TS*3,TS*41+4),(TS*4,TS*47+4),(TS*13,TS*53+4)]

       def display(self):
           screen.blit(font_menu.render("Normal Mode", False, pygame.Color('White')),(TS*7,TS*41))
           screen.blit(font_menu.render("Gamer Mode", False, pygame.Color('White')),(TS*8,TS*47))
           screen.blit(font_menu.render("Return", False, pygame.Color('White')),(TS*17,TS*53))

   class Settings_Menu():

       def __init__(self):
           self.size = 1
           self.type = "Settings Menu"
           self.positions = [(TS*7,TS*44+4),(TS*13,TS*50+4)]

       def display(self):
           global game_volume
           screen.blit(font_menu.render("Volume", False, pygame.Color('White')),(TS*11,TS*44))
           screen.blit(font_menu.render(str(game_volume), False, pygame.Color('White')),(300,TS*44))
           screen.blit(font_menu.render("Return", False, pygame.Color('White')),(TS*17,TS*50))

   class Credits_Menu():

       def __init__(self):
           self.size = 0
           self.type = "Credits Menu"
           self.positions = [(TS*19,490)]

       def display(self):
           screen.blit(font.render("This game was made as a", False, pygame.Color('White')),(TS*4,288))
           screen.blit(font.render("college project for UFCG", False, pygame.Color('White')),(TS*4,304))
           screen.blit(font.render("Developers:", False, pygame.Color('White')),(TS*4,336))
           screen.blit(font.render("Abraao Caiana de Freitas", False, pygame.Color('White')),(TS*4,368))
           screen.blit(font.render("Augusto Nunes Zacarias", False, pygame.Color('White')),(TS*4,400))
           screen.blit(font.render("Davi Henrique Silva", False, pygame.Color('White')),(TS*4,432))
           screen.blit(font.render("Joao Gabriel Abrantes", False, pygame.Color('White')),(TS*4,464))
         
           screen.blit(font.render("Return", False, pygame.Color('White')),(TS*23,496))

   class Cursor():
       
       def __init__(self):
           self.arrow = load_img('arrow.png')
           self.index = 0
           self.direction = STOP
           self.size_menu = 3

       def move(self):
           global game_volume
           self.size_menu=menu.size

           if self.direction == RIGHT:
              if menu.type=="Settings Menu" and self.pos()==menu.positions[0]:
                 if game_volume<100:
                    game_volume+=10
           elif self.direction == LEFT:
              if menu.type=="Settings Menu" and self.pos()==menu.positions[0]:
                 if game_volume>0:
                    game_volume-=10
           elif self.direction == DOWN:
               if self.index == self.size_menu:
                   self.index = 0
               else:
                   self.index += 1
           elif self.direction == UP:
               if self.index == 0:
                   self.index = self.size_menu
               else:
                   self.index -= 1

           self.direction = STOP
       def pos(self):
           return menu.positions[self.index]

       def display(self):
           screen.blit(self.arrow,self.pos())
       
   class Animation():

       def __init__(self):
           self.pos=(TS*1,TS*29) #starting postion
           self.img=patoAD #starting image
           self.aberto=True #Variable to make mouth open and close

       def animate(self):
           self.aberto=not self.aberto 
           screen.blit(self.img,self.pos)
           if self.pos[1]==TS*67 and TS*2<=self.pos[0]<=TS*52:
               self.img=patoAE if self.aberto else patoFE
               self.pos=(self.pos[0]-TS,self.pos[1]) #moves left

           elif self.pos[0]==TS*52 and TS*66>=self.pos[1]>=TS*29:
               self.img=patoAB if self.aberto else patoFB
               self.pos=(self.pos[0],self.pos[1]+TS) #moves down

           elif self.pos[1]==TS*29 and TS*51>=self.pos[0]>=TS*1:
               self.img=patoAD if self.aberto else patoFD
               self.pos=(self.pos[0]+TS,self.pos[1]) #moves right

           elif self.pos[0]==TS*1 and TS*68>=self.pos[1]>=TS*30:
               self.img=patoAC if self.aberto else patoFC
               self.pos=(self.pos[0],self.pos[1]-TS) #moves up

   #creating classes        
   header=Header()
   animation=Animation()
   menu=Main_Menu()
   cursor=Cursor()

   main_menu = True
   start_menu = False
   settings_menu = False
   credits_menu = False

   while True:
       clock.tick(15)

       for event in pygame.event.get():

               if event.type == pygame.QUIT:
                   pygame.quit() #Quit game

               #Directions keys
               if event.type == KEYDOWN:
                   if event.key == K_UP:
                       cursor.direction = UP
                   if event.key == K_DOWN:
                       cursor.direction = DOWN
                   if event.key == K_LEFT:
                       cursor.direction = LEFT
                   if event.key == K_RIGHT:
                       cursor.direction = RIGHT
                   
                   if event.key == K_RETURN:
                       if menu.type == "Main Menu":
                           if cursor.index == 0:
                               menu = Start_Menu()
                           elif cursor.index == 1:
                               menu = Settings_Menu()
                           elif cursor.index == 2:
                               menu = Credits_Menu()
                           elif cursor.index == 3:
                               pygame.quit()
                           cursor.index = 0 #initialize cursor on the top of new menu

                       elif menu.type == "Start Menu":
                           if cursor.pos() == menu.positions[0]:   #start level 1
                               level1.game(game_volume/200,game_speed=15,diff="easy")
                           elif cursor.pos() == menu.positions[1]: #start level 1
                               level1.game(game_volume/200,game_speed=30,diff="hard")
                           elif cursor.pos() == menu.positions[2]: #return buttom
                               menu = Main_Menu()
                           cursor.index = 0 #reinitialize cursor in the main menu on the right position

                       elif menu.type == "Settings Menu":
                           if cursor.pos() == menu.positions[0]: #already handled in cursor.move
                               pass
                           if cursor.pos() == menu.positions[1]: #return buttom
                               menu = Main_Menu()
                           cursor.index = 1 #reinitialize cursor in the main menu on the right position

                       elif menu.type == "Credits Menu":
                           if cursor.pos() == menu.positions[0]: #return buttom
                               menu = Main_Menu()
                           cursor.index = 2 #reinitialize cursor in the main menu on the right position

       screen.fill((0, 0, 0)) #Display objects on screen
       header.display() #Displays header
       animation.animate() #Shows duck animation
       cursor.move() #Moves cursor
       cursor.display() #Displays cursor

       if main_menu == True:
           menu.display() #Displays menu
       pygame.display.update()

if __name__=='__main__':
   run()
