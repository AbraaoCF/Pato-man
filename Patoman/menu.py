import pygame
import os
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]

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

patoFC = load_img('patoFC.png')
patoFD = load_img('patoFD.png')
patoFB = load_img('patoFB.png')
patoFE = load_img('patoFE.png')
patoAC = load_img('patoAC.png')
patoAD = load_img('patoAD.png')
patoAB = load_img('patoAB.png')
patoAE = load_img('patoAE.png')
    
TS=8

pygame.init()

screen = pygame.display.set_mode((TS * 56, TS * 72))
pygame.display.set_caption("Pato-man")

clock = pygame.time.Clock()

font=load_font("emulogic.ttf")

class Header():

    def __init__(self):
        self.title=load_img('patoman_logo.png');


    def display(self):
        screen.blit(font.render("Controls: -Arrows to move",False,pygame.Color('White')),(16,176))
        screen.blit(font.render("          -Enter to select",False,pygame.Color('White')),(16,192))
        screen.blit(font.render("          -Esc to pause",False,pygame.Color('White')),(16,208))
        screen.blit(self.title,(81,64))

class Animation():

    def __init__(self):
        pass
    
header=Header()
while True:
    clock.tick(15)

    for event in pygame.event.get():

            #Quit game
            if event.type == pygame.QUIT:
                pygame.quit()

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

    #Display objects on screen
    screen.fill((0, 0, 0))
    header.display()


    pygame.display.update()
