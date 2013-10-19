
# Copyright (c) 2013 Johan Ceuppens.
# All rights reserved.

# Redistribution and use in source and binary forms are permitted
# provided that the above copyright notice and this paragraph are
# duplicated in all such forms and that any documentation,
# advertising materials, and other materials related to such
# distribution and use acknowledge that the software was developed
# by the Johan Ceuppens.  The name of the
# Johan Ceuppens may not be used to endorse or promote products derived
# from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

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

class Box(Gameobject):
    "Box"
    def __init__(self, xx,yy,ww,hh):
        Gameobject.__init__(self,xx,yy)
        self.w = ww
        self.h = hh
        self.hitpoints = 999999999 #FIX else wall/floor disappears
        #FIX is in base class 
	#self.image = pygame.image.load('./pics/.bmp').convert()
        #self.image.set_colorkey((0,0,0)) 

    def setimage(self, imagefilename,r,g,b):
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((r,g,b)) 

    def collide(self, room, player, hploss):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey + player.hforplatform and #FIXED +self.h
	player.y < self.y+room.relativey):
	    print "collision in box!"	
	    return 1 
	else:
	    return 0


    def fallcollide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey+player.h > self.y and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0 ## for game self.talker
