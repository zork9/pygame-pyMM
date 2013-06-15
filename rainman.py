
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

class Rainman(Gameobject):
    "Spider"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 50
        self.h = 50 
        self.hitpoints = 2 
        
        self.yy = yy
    
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/rainman-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/rainman-2.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/rainman-3.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)

	self.direction = "none"

    def draw(self, screen, room):
	self.stimlib.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
	    
    def update(self,room,player):
	if player.x + room.relativex < self.x:
		self.direction = "left"
	else:
		self.direction = "right"

	if self.direction == "left":
		self.x -= 2
	elif self.direction == "right":	
		self.x += 2
	   


    def fight(self,room,player,keydown = -1):
        1
