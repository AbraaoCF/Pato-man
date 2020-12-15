import pygame
import os
from pygame.locals import *
from Patoman import main as level1

main_dir = os.path.split(os.path.abspath(__file__))[0]

game_volume=50
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

def play_music(name,volume):
   path=os.path.join(main_dir,"sounds",name)
   pygame.mixer.music.load(path)
   pygame.mixer.music.set_volume(volume)
   pygame.mixer.music.play(loops=-1)


def run():
   
   pygame.init() #initializing pygame
   if not pygame.mixer.get_init():
       pygame.mixer.init()

   # Limitations (inclusive) for menu options:
   #top: 256 bottom: 528
   #left: 32 right: 400

   #Directions
   UP    = 0
   LEFT  = 1
   DOWN  = 2
   RIGHT = 3
   STOP  = 4

   #loading images
   patoFC = load_img('patoFC.png')
   patoFD = load_img('patoFD.png')
   patoFB = load_img('patoFB.png')
   patoFE = load_img('patoFE.png')
   patoAC = load_img('patoAC.png')
   patoAD = load_img('patoAD.png')
   patoAB = load_img('patoAB.png')
   patoAE = load_img('patoAE.png')
   arrow = load_img('arrow.png')
   
   font=load_font("emulogic.ttf",16)
   font_menu=load_font("emulogic.ttf",32)

   screen = pygame.display.set_mode((448, 576)) #sets screen size
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
         self.positions=[(120,308),(72,356),(96,404),(128,452)]
     
      def display(self):
         screen.blit(font_menu.render("Start", False, pygame.Color('White')),(152,304))
         screen.blit(font_menu.render("Settings", False, pygame.Color('White')),(104,352))
         screen.blit(font_menu.render("Credits", False, pygame.Color('White')),(120,400))
         screen.blit(font_menu.render("Quit", False, pygame.Color('White')),(160,448))

   class Start_Menu():

      def __init__(self):
         self.size = 2
         self.type = "Start Menu"
         self.positions = [(24,332),(32,380),(104,428)]

      def display(self):
         screen.blit(font_menu.render("Normal Mode", False, pygame.Color('White')),(56,328))
         screen.blit(font_menu.render("Gamer Mode", False, pygame.Color('White')),(64,376))
         screen.blit(font_menu.render("Return", False, pygame.Color('White')),(136,424))

   class Settings_Menu():

      def __init__(self):
         self.size = 1
         self.type = "Settings Menu"
         self.positions = [(56,356),(104,404)]

      def display(self):
         global game_volume
         screen.blit(font_menu.render("Volume", False, pygame.Color('White')),(88,352))
         screen.blit(font_menu.render(str(game_volume), False, pygame.Color('White')),(300,352))
         screen.blit(font_menu.render("Return", False, pygame.Color('White')),(136,400))

   class Credits_Menu():

      def __init__(self):
         self.size = 0
         self.type = "Credits Menu"
         self.positions = [(152,490)]

      def display(self):
         screen.blit(font.render("This game was made as a", False, pygame.Color('White')),(32,288))
         screen.blit(font.render("college project for UFCG", False, pygame.Color('White')),(32,304))
         screen.blit(font.render("Developers:", False, pygame.Color('White')),(32,336))
         screen.blit(font.render("Abraao Caiana de Freitas", False, pygame.Color('White')),(32,368))
         screen.blit(font.render("Augusto Nunes Zacarias", False, pygame.Color('White')),(32,400))
         screen.blit(font.render("Davi Henrique Silva", False, pygame.Color('White')),(32,432))
         screen.blit(font.render("Joao Gabriel Abrantes", False, pygame.Color('White')),(32,464))
         
         screen.blit(font.render("Return", False, pygame.Color('White')),(184,496))

   class Cursor():
       
      def __init__(self):
         self.image = arrow
         self.index = 0
         self.direction = STOP
         self.size_menu = 3

      def move(self):
         global game_volume
         self.size_menu=menu.size
         if pygame.mixer.get_init():
            pygame.mixer.stop()
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
         screen.blit(self.image,self.pos())
       
   class Animation():

      def __init__(self):
         self.pos=(8,232) #starting postion
         self.img=patoAD #starting image
         self.aberto=True #Variable to make mouth open and close

      def animate(self):
         self.aberto=not self.aberto 
         screen.blit(self.img,self.pos)
         if self.pos[1]==536 and 10<=self.pos[0]<=416:
            self.img=patoAE if self.aberto else patoFE
            self.pos=(self.pos[0]-2,self.pos[1]) #moves left

         elif self.pos[0]==416 and 534>=self.pos[1]>=232:
            self.img=patoAB if self.aberto else patoFB
            self.pos=(self.pos[0],self.pos[1]+2) #moves down

         elif self.pos[1]==232 and 414>=self.pos[0]>=8:
            self.img=patoAD if self.aberto else patoFD
            self.pos=(self.pos[0]+2,self.pos[1]) #moves right

         elif self.pos[0]==8 and 544>=self.pos[1]>=230:
            self.img=patoAC if self.aberto else patoFC
            self.pos=(self.pos[0],self.pos[1]-2) #moves up

   #creating classes        
   header=Header()
   animation=Animation()
   menu=Main_Menu()
   cursor=Cursor()

   main_menu = True
   start_menu = False
   settings_menu = False
   credits_menu = False
   play_music('menu_music.wav',game_volume/200)
   while True:
      clock.tick(40)

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
                  
                  cursor.index = 0 #reinitialize cursor on the top of new menu

               elif menu.type == "Start Menu":
                  if cursor.pos() == menu.positions[0]:   #start level 1
                     level1.setup(game_volume/200,False)
                  elif cursor.pos() == menu.positions[1]: #start level 1
                     level1.setup(game_volume/200,True)
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
      pygame.mixer.music.set_volume(game_volume/200)#update menu song volume

      if main_menu == True:
         menu.display() #Displays menu
      pygame.display.update()

if __name__=='__main__':
   run()
