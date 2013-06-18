# Copyright (C) Johan Ceuppens 2010-2013
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from pygame.locals import *
from gameobject import *
from stateimagelibrary import *
import random
from os import *
from time import *
from random import *
from math import *
from rng import *
from heatmansflamerow1 import *
from heatmansflamerow2 import *
from heatmansflamerow3 import *
from heatmansflamerow4 import *

class HeatMan(Gameobject):
	"Heat Man"
	def __init__(self, xx, yy):
		Gameobject.__init__(self,xx,yy)
		self.w = 80
		self.h = 80
		self.hitpoints = 450

		self.yy = yy

		self.stimlibflamingleft = Stateimagelibrary()
		image = pygame.image.load('./pics/heatman-flaming-left-1.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-2.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-3.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-4.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-5.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-6.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-7.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-8.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingleft.addpicture(image)

		self.stimlibflamingright = Stateimagelibrary()
		image = pygame.image.load('./pics/heatman-flaming-left-1.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-2.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-3.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-4.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-5.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-6.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-7.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)
		image = pygame.image.load('./pics/heatman-flaming-left-8.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibflamingright.addpicture(image)

		self.stimlibshootingleft = Stateimagelibrary()
		image = pygame.image.load('./pics/heatman-shooting-1.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibshootingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-shooting-2.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibshootingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-shooting-3.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibshootingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-shooting-4.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibshootingleft.addpicture(image)
		image = pygame.image.load('./pics/heatman-shooting-5.bmp').convert()
		image.set_colorkey((0,0,0))
		self.stimlibshootingleft.addpicture(image)

		self.direction = 1 ### NOTE 1 left, 0 right direction
		self.flamingcounter = 0
		self.shootingcounter = 0

	def draw(self,screen,room):
		if self.direction == 0:
			if randint(0,100) == 100 and self.flamingcounter == 0:
				self.stimlibflamingright.draw(screen,self.x-40+room.relativex,self.y+room.relativey)
				self.flamingcounter += 1
			elif self.flamingcounter > 0:
				self.stimlibflamingright.draw(screen,self.x-40+room.relativex,self.y+room.relativey)
				
			return	
		if self.direction == 1:
			if randint(0,100) == 100 and self.flamingcounter == 0:
				self.stimlibflamingleft.draw(screen,self.x-40+room.relativex,self.y+room.relativey)
				self.flamingcounter += 1
			elif self.flamingcounter > 0:
				self.stimlibflamingleft.draw(screen,self.x-40+room.relativex,self.y+room.relativey)
				if self.flamingcounter >= 8:
					self.flamingcounter = 0	
			if randint(0,10) == 10 and self.shootingcounter == 0:
				self.stimlibshootingleft.draw(screen,self.x-40+room.relativex,self.y+room.relativey)
			elif self.shootingcounter > 0:
				self.stimlibshootingleft.draw(screen,self.x-40+room.relativex,self.y+room.relativey)

				if self.shootingcounter >= 25:
					self.shootingcounter = 0	
				elif self.shootingcounter >= 20:
					room.gameobjects.append(HeatMansFlamerow4(self.x-40+room.relativex,self.y+room.relativey,"left"))
				elif self.shootingcounter >= 15:
					room.gameobjects.append(HeatMansFlamerow3(self.x-40+room.relativex,self.y+room.relativey,"left"))
				elif self.shootingcounter >= 10:
					room.gameobjects.append(HeatMansFlamerow2(self.x-40+room.relativex,self.y+room.relativey,"left"))
				elif self.shootingcounter >= 5:
					room.gameobjects.append(HeatMansFlamerow1(self.x-40+room.relativex,self.y+room.relativey,"left"))
					
			return	
		self.stimlibflamingleft.drawstatic(screen,self.x-40+room.relativex,self.y+room.relativey,0)	



	def update(self,room,player):
		1

	def fight(self,room,player,keydown = 1):
		1


