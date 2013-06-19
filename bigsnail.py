
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
from rng import *

class BigSnail(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 180
        self.h = 110 
        self.hitpoints = 6

	self.eyesclosedcounter = 0
        
        self.yy = yy
    
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/snail-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)

        self.stimlibeyesclosed = Stateimagelibrary()	
        image = pygame.image.load('./pics/snail-left-eyesclosed-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibeyesclosed.addpicture(image)

    def draw(self, screen, room):
	self.eyesclosedcounter += 1
	if self.eyesclosedcounter > 23:
        	self.stimlibeyesclosed.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
		if self.eyesclosedcounter > 26:
			self.eyesclosedcounter = 0
	else:
	        self.stimlib.draw(screen, self.x-40+room.relativex,self.y+room.relativey)
	    
    def update(self,room,player):
	1

    def collide(self, room, player,hploss):
        # FIX BUG
        # print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with BigSnail!"
	    player.hitpoints -= hploss
	    return 1 
	else:
	    return 0 ## for game self.talker

    def fight(self,room,player,keydown = -1):
        1
