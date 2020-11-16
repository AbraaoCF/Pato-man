import pygame
import os
from pygame.locals import *

pygame.init() #initializing pygame
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Limitations (inclusive) for menu options:
#top: TS*32 bottom: TS*66
#left: TS*4 right: TS*50

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

while True:
    clock.tick(15)

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit() #Quit game

            #Directions keys
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                    #player.direct = UP
                if event.key == K_DOWN:
                    pass
                    #player.direct = DOWN
                if event.key == K_LEFT:
                    pass
                    #player.direct = LEFT
                if event.key == K_RIGHT:
                    pass
                    #player.direct = RIGHT

    screen.fill((0, 0, 0)) #Display objects on screen
    header.display() #displays header
    animation.animate() # shows duck animation

    pygame.display.update()
