
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
from os import *
from time import *
from math import *
from random import *
from rng import *

# This is kludgy but fast

class ToadMan(Gameobject):
    "Toad Man"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 50
        self.h = 50 
        self.hitpoints = 15 
        
        self.yy = yy
    
        self.stimlibleft = Stateimagelibrary()	
        image = pygame.image.load('./pics/toadman-static-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/toadman-preparing-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/toadman-duck-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/toadman-jump-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)

        self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/toadman-static-right-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/toadman-preparing-right-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/toadman-duck-right-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/toadman-jump-right-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)

	###self.jumpradius = 7 
	self.jumpradius = 17 
	self.factor = 5
	self.yoffset = 100 
	self.y = sqrt(abs(self.x*self.x*5 - self.jumpradius*self.jumpradius))/self.factor ####FIXME all + 200
	self.y += self.yoffset ##KLUDGE
	###self.x += 100
	self.startx = self.x
	self.starty = self.y
	self.jumping = 0
	self.direction = 1 ## facing left is 1, right is 0 

	self.jx = self.x


    def draw(self, screen, room):
	###FIXME self.stimlib.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
	if self.direction == 1:
		self.stimlibleft.drawstatic(screen, self.x,self.y,0)
	elif self.direction == 0:
		self.stimlibright.drawstatic(screen, self.x,self.y,0)
	    
    def update(self,room,player):
	if randint(0,10) == 10 and self.jumping == 0:
		self.jumping = -1
	if self.jumping < 0 and self.direction == 1:
		#print "x=%d y=%f" % (self.x,self.y)
		if self.starty - self.y < 200 + self.yoffset:
			self.x -= 7
			self.jx -= 7
			self.y = sqrt(abs(self.jx*self.jx*5 - self.jumpradius*self.jumpradius)) / self.factor
			self.x += 5
			###self.y += 200

			if abs(self.x - self.startx) > 285:
				self.jumping = 0
				self.y = self.starty
				self.direction = 0
				self.startx = self.x
	
	if self.jumping < 0 and self.direction == 0:
		#print "x=%d y=%f" % (self.x,self.y)
		if self.starty - self.y < 200 + self.yoffset:
			self.x += 7
			self.jx += 7
			self.y = sqrt(abs(self.jx*self.jx*5 - self.jumpradius*self.jumpradius)) / self.factor
			self.x -= 5
			###self.y += 200

			if abs(self.x - self.startx) > 285:
				self.jumping = 0
				self.y = self.starty
				self.direction = 1
				self.startx = self.x

    def fight(self,room,player,keydown = -1):
        1

