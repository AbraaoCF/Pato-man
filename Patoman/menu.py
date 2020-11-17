import pygame
import os
from pygame.locals import *

pygame.init() #initializing pygame
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Limitations (inclusive) for menu options:
#top: TS*32 bottom: TS*66
#left: TS*4 right: TS*50

#Directions
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3
STOP  = 4

def load_img(name):
   path=os.path.join(main_dir,"imgs",name)
   return pygame.image.load(path)

def load_sound(name):
   path=os.path.join(main_dir,"sounds",name)
   this_sound = pygame.mixer.Sound(path)
   this_sound.set_volume(0.3)
   return this_sound

def load_font(name):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,16)

def load_font_menu(name):
   path=os.path.join(main_dir,"fonts",name)
   return pygame.font.Font(path,28)

#loading resources
patoFC = load_img('patoFC.png')
patoFD = load_img('patoFD.png')
patoFB = load_img('patoFB.png')
patoFE = load_img('patoFE.png')
patoAC = load_img('patoAC.png')
patoAD = load_img('patoAD.png')
patoAB = load_img('patoAB.png')
patoAE = load_img('patoAE.png')

font=load_font("emulogic.ttf")
font_menu=load_font_menu("emulogic.ttf")
TS=8 #setting the size in pixels of a tile

screen = pygame.display.set_mode((TS * 56, TS * 72)) #sets screen size
pygame.display.set_caption("Pato-man") #sets screen title

clock = pygame.time.Clock() #create clock object

class Header():

    def __init__(self):
        self.title=load_img('patoman_logo.png'); #defines title image


    def display(self):
        #writes text to screen
        screen.blit(font.render("Controls: -Arrows to move",False,pygame.Color('White')),(16,176))
        screen.blit(font.render("          -Enter to select",False,pygame.Color('White')),(16,192))
        screen.blit(font.render("          -Esc to pause",False,pygame.Color('White')),(16,208))
        screen.blit(self.title,(81,64)) #shows title image

class Main_Menu():

    def __init__(self):
        pass

    def display(self):
        screen.blit(font_menu.render("Start", False, pygame.Color('White')),(82,288))
        screen.blit(font_menu.render("Settings", False, pygame.Color('White')),(82,322))
        screen.blit(font_menu.render("Credits", False, pygame.Color('White')),(82,358))
        screen.blit(font_menu.render("Quit", False, pygame.Color('White')),(82,394))

class Cursor():
    
    def __init__(self):
        self.arrow = load_img('right_arrow.png')
        self.start = (62,296) #Cursor pointing to 'start' 
        self.settings = (62,330) #Cursor pointing to 'settings'
        self.credits = (62,366) #Cursor pointing to 'credits'
        self.quit = (62,402) #Cursor pointing to 'quit'
        self.pos = self.start
        self.direction = STOP

    def move(self):
        if self.direction == STOP or self.direction == RIGHT or self.direction == LEFT:
            pass
        elif self.direction == UP:
            if self.pos == self.start:
                self.pos = self.quit
            elif self.pos == self.settings:
                self.pos = self.start
            elif self.pos == self.credits:
                self.pos = self.settings
            elif self.pos == self.quit:
                self.pos = self.credits
        elif self.direction == DOWN:
            if self.pos == self.quit:
                self.pos = self.start
            elif self.pos == self.start:
                self.pos = self.settings
            elif self.pos == self.settings:
                self.pos = self.credits
            elif self.pos == self.credits:
                self.pos = self.quit
        self.direction = STOP

    def display(self):
        screen.blit(self.arrow,self.pos)

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
             
    screen.fill((0, 0, 0)) #Display objects on screen
    header.display() #Displays header
    menu.display() #Displays menu
    animation.animate() #Shows duck animation
    cursor.move()#Moves cursor
    cursor.display()#Displays cursor
    pygame.display.update()
