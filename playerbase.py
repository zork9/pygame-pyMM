

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
from stateimagelibrary import *

#class PlayerBase:
#    def __init__(self):
#        1

#class PlayerBase(PlayerBase,PlayerBase):
class PlayerBase:
    "Player"

    def __init__(self,heartmeter):
	self.heartmeter = heartmeter
	self.direction = "none"
	self.prevdirection = "right"
        self.x = 280 
        self.y = 300 
        self.w = 50 
        self.h = 50
	self.hforplatform = 50  ### NOTE 
        self.fightcounter = 0

	self.hurt = 0

    def drawstatic(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
	self.stimlib.drawstatic(screen,self.x,self.y,0)

    def drawclimbing(self, screen):
	self.stimlibclimbing.draw(screen,self.x,self.y)

    def drawclimbingstatic(self, screen):
	self.stimlibclimbing.drawstatic(screen,self.x,self.y,0)

    def drawduck(self, screen):
	self.stimlibduck.draw(screen,self.x,self.y)
	
    def draw(self, screen):
	if self.hurt > 0:
		self.hurt += 1
		if self.direction == "left": 
            		self.stimlibhurt.drawstatic(screen,self.x,self.y,0)
		elif self.direction == "right": 
            		self.stimlibhurt.drawstatic(screen,self.x,self.y,1)
		if self.hurt > 3:
			self.hurt = 0
            	return
			
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return

	if self.direction == "right":
        	self.stimlib.draw(screen, self.x,self.y)
	elif self.direction == "left":
		self.stimlibleft.draw(screen,self.x,self.y)



    def fight(self,room):
        self.fightcounter = 1
##        self.x -= 30
##        self.y -= 30
##        self.w += 30
##        self.h += 30
        
        o = room.collidesword(room,self)
        
        if o:
            print 'hit!'
            room.hitwithsword(o)
##        self.x += 30
##        self.y += 30
##        self.w -= 30
##        self.h -= 30
##

        
    def hit(self):##overrriden in playermegaman.py
	self.heartmeter.index -= 1
	self.hurt = 1
	if self.heartmeter.index <= 0:
		return 0 #FIXME1 FIX for gameover when collision with enemies 
	else:
		return 1	

    def askclass(self):
        return "Fighter"

    def askrace(self):
        return "Human"

    def askpicture(self):
        return './pics/taskbar-PC.bmp'

