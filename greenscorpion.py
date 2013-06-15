
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
from stateimagelibrary import *
import random
from time import *
from math import *
from random import *
from rng import *

class GreenScorpion(Gameobject):
    "Spider"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 50
        self.h = 50 
        self.hitpoints = 2 
        
        self.yy = yy
    
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/scorpion-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/scorpion-left-2.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/scorpion-left-3.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)

        self.stimlibwirr = Stateimagelibrary()	
        image = pygame.image.load('./pics/scorpion-left-wirring-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibwirr.addpicture(image)

	self.wirrcount = 0
	self.direction = "none"

    def draw(self, screen, room):
	if self.wirrcount >= 1:
	       	self.stimlibwirr.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
        else:
		self.stimlib.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
	    
    def update(self,room,player):
           if self.wirrcount == 0 and randint(0,10) == 10:
		if randint(0,1):
			self.direction = "left"
		else:
			self.direction = "right"
		self.wirrcount = 1

	   if self.wirrcount > 10:
		self.wirrcount = 0 
	   if self.wirrcount > 0:
		self.wirrcount += 1
		if self.direction == "left":
			self.x -= 2
		else:
			self.x += 2
	   


    def fight(self,room,player,keydown = -1):
        1
