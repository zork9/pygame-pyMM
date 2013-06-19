
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

class Ladder:
    "ladder"
    def __init__(self, xx,yy,ww,hh,imagefilename):
	self.x = xx
        self.y = yy 
        self.w = ww 
        self.h = hh
        
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((0,0,0)) 
        self.hitpoints = 999999

       	self.ladderoffsetup = 50
       	self.ladderoffsetup2 = 50
 
    def draw(self, screen, room):
        screen.blit(self.image,(self.x+room.relativex+self.w*2,self.y+room.relativey))
	    
	     
    def collidewithladder(self, room, player):
        # print 'rope x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y - self.ladderoffsetup and
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Ladder!"
	    return 1 
	else:
	    return 0


	## For entering the ladder down wise

    def collidewithladderdown(self, room, player):
        # print 'rope x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > (self.y - self.ladderoffsetup - self.ladderoffsetup2) and
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Ladder!"
	    return 1 
	else:
	    return 0
    
    
    def update(self,room,player):
	1
