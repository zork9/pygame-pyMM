
# Copyright (C) Johan Ceuppens 2010
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
from bullet import *
from stateimagelibrary import *
import random
from time import *
from math import *
from random import *
from rng import *

class BomberToad(Gameobject):
    "Dude on Toad throwing Bombs"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 100
        self.h = 100 
        self.hitpoints = 2 
        
        self.yy = yy
    
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/bomber-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/bomber-left-2.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/bomber-left-3.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/bomber-left-4.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)

	self.counter = 0

    def draw(self, screen, room):
	if randint(0,100) != 100 and self.counter == 0:
		self.counter = 0
		self.stimlib.drawstatic(screen, self.x-40+room.relativex,self.y+room.relativey, 0)
	else:
		self.counter += 1
		self.stimlib.drawstatic(screen, self.x-40+room.relativex,self.y+room.relativey, self.counter)
	   	if self.counter >= 3:
			self.counter = 0
			room.gameobjects.append(Bullet(self.x+room.relativex,self.y+room.relativey, "left"))
 
    def update(self,room,player):
	  1 


    def fight(self,room,player,keydown = -1):
        1
