import random
import pygame
from pygame.locals import *
import Matriz

matriz = Matriz.mat();

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

Inky = 0
Blinky = 1
Clyde = 2
Pinky = 3

SCATTER = 0
CHASE = 1
EATEN = 2
FRIGHTENED = 3

TS = 8

Blinky_img = pygame.Surface((16,16))
Blinky_img.fill((255,0,0))

Inky_img = pygame.Surface((16,16))
Inky_img.fill((19,249,226))

Clyde_img = pygame.Surface((16,16))
Clyde_img.fill((209,239,13))

Pinky_img = pygame.Surface((16,16))
Pinky_img.fill((218,15,245))

class Ghost(pygame.sprite.Sprite):
	
	def __init__(self, type_ghost):
		self.ghost = type_ghost
		
		if(self.ghost == Inky):
			self.pos = (6*TS,8*TS)
			self.img = Inky_img
		if(self.ghost == Blinky):
			self.pos = (2*TS,8*TS)
			self.img = Blinky_img
		if(self.ghost == Clyde):
			self.pos = (2*TS,8*TS)
			self.img = Clyde_img
		if(self.ghost == Pinky):
			self.pos = (2*TS,8*TS)
			self.img = Pinky_img
		
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.img.get_rect()
		self.rect.x = 6*TS
		self.rect.y = 8*TS
		self.direct = LEFT
	
	def dis(self, x, y):
		return (self.target[0] - x) ** 2 + (self.target[1] - y) ** 2
	
	def move(self, x, y, direct, redx, redy):
		possible_moviments = []
		
		if(self.mode == SCATTER):
			if(self.ghost == Inky):
				self.target = (71, 55)
			if(self.ghost == Blinky):
				self.target = (-1, 52)
			if(self.ghost == Clyde):
				self.target = (71, 0)
			if(self.ghost == Pinky):
				self.target = (-1, 4)
			
			#Find possible Moviments for Ink
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]// TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]

		if(self.mode == FRIGHTENED):
		
			#Find possible Moviments for Ink
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS + 1) % 56, RIGHT])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56, LEFT])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.pos[1] // TS + 1, self.pos[0] // TS, DOWN])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)): can = False
				
				if(can):
					possible_moviments.append([self.pos[1] // TS - 1, self.pos[0] // TS, UP])
			
			#Choose a random direction
			random_direct = random.choice(possible_moviments)
			self.pos = (random_direct[1] * TS, random_direct[0] * TS)
			self.rect.x = random_direct[1] * TS
			self.rect.y = random_direct[0] * TS
			self.direct = random_direct[2]
		
		if(self.mode == EATEN):
			self.target = (29, 27)
			
			#Find possible Moviments for Ink
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
		
		if(self.mode == CHASE):
			if(self.ghost == Inky):
				self.target = (x - (redx - x), y - (redy - y))
				
				#print(f"Target: {self.target[0]}, {self.target[1]}, Player: {x}, {y}")
				
			if(self.ghost == Blinky):
				self.target = (x, y)
			if(self.ghost == Clyde):
				self.target = (x, y)
				if(self.dis(self.pos[1] // TS, self.pos[0] // TS) < 256):
					self.target = (71, 0)
			if(self.ghost == Pinky):
				if(direct == LEFT):
					self.target = (x, y - 8)
				if(direct == RIGHT):
					self.target = (x, y + 8)
				if(direct == DOWN):
					self.target = (x + 8, y)
				if(direct == UP):
					self.target = (x - 8, y - 8)		
			#Find possible Moviments for Ink
			if(self.direct != LEFT and matriz[self.pos[1] // TS][(self.pos[0] // TS + 1) % 56] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0] // TS + 1) % 56), RIGHT, self.pos[1] // TS, (self.pos[0] // TS + 1) % 56])
			if(self.direct != RIGHT and matriz[self.pos[1] // TS][self.pos[0] // TS - 1] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS, (self.pos[0]//TS - 1 + 56) % 56), LEFT, self.pos[1] // TS, (self.pos[0] // TS - 1 + 56) % 56])
			if(self.direct != UP and matriz[self.pos[1] // TS + 1][self.pos[0] // TS] != 1):
				possible_moviments.append([self.dis(self.pos[1] // TS + 1, self.pos[0] // TS), DOWN, self.pos[1] // TS + 1, self.pos[0] // TS])
			if(self.direct != DOWN and matriz[self.pos[1] // TS - 1][self.pos[0] // TS] != 1):
				
				can = True
				
				if((self.pos[1] // TS - 1 == 27 or self.pos[1] // TS - 1 == 51) and (self.pos[0] // TS == 24 or self.pos[0] // TS == 30)):
					can = False
				
				if(can):
					possible_moviments.append([self.dis(self.pos[1] // TS - 1, self.pos[0] // TS), UP, self.pos[1] // TS - 1, self.pos[0] // TS])
			
			#Calculate better moviment
			possible_moviments.sort()
			
			self.pos = (possible_moviments[0][3] * TS, possible_moviments[0][2] * TS)
			self.rect.x = possible_moviments[0][3] * TS
			self.rect.y = possible_moviments[0][2] * TS
			self.direct = possible_moviments[0][1]
		
	def display(self):
		screen.blit(self.img,(self.pos[0]-4,self.pos[1]-8))
		
