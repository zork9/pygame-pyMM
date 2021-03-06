

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
from maproomdungeon import *
from bigsnail import *
from wall import *
from ladder import *
from imagebox import *
from skeletondrone import *
from greenscorpion import *
from rainman import *
from bombertoad import *
from toadman import *

class Maproom1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/bg2-2400x600.bmp').convert()

	self.w = 2400
	self.h = 480

	self.mapoffsetx = 400

        ###self.northwall1 = Tilebox(1,1,60,48,16,1,'./pics/walldungeonnorth2-beholderglass-60x48.bmp')
##        self.northwall1 = Tilebox(1,1,60,48,13,1,'./pics/walldungeonnorth1-60x48.bmp')
##        self.southwall1 = Tilebox(1,200,30,48,13,1,'./pics/walldungeonsouth1-30x48.bmp')
##        self.westwall1 = Tilebox(360,200,48,60,1,10,'./pics/walldungeonwest1-48x60.bmp')
##        self.eastwall1 = Tilebox(775,1,48,60,1,14,'./pics/walldungeoneast1-48x60.bmp')
##        self.tileboxes.append(self.northwall1)
##        self.tileboxes.append(self.westwall1)
##        self.tileboxes.append(self.eastwall1)
##        self.tileboxes.append(self.southwall1)

        self.gameobjects.append(BomberToad(2000,420))
        self.gameobjects.append(Rainman(1000,140))
        self.gameobjects.append(GreenScorpion(600,320))
        self.gameobjects.append(GreenScorpion(700,320))
        self.gameobjects.append(GreenScorpion(800,320))
        self.gameobjects.append(GreenScorpion(1000,320))
        self.gameobjects.append(BigSnail(830,92))
        self.gameobjects.append(BigSnail(2425,600))
        
        # left NOTE : boxes collide so put them after enemies !
	### walls 
        self.addeastwall(2700,0,50,600,"./pics/wall-level1-50x500.bmp")

	### roof box
        self.gameobjects.append(ImageBox(0,50,2400,45,"./pics/platform-265x50-1.bmp"))
        self.gameobjects.append(Box(0,400,1300,250))
        self.gameobjects.append(Box(1280,460,300,25))### FIXME some 25 -> 250
        self.gameobjects.append(Box(1580,550,300,25))
        self.gameobjects.append(Box(1920,560,300,25))
        self.gameobjects.append(Box(2250,560,150,25))
	# First BigSnail sits here
        self.gameobjects.append(ImageBox(0,200,265,25,"./pics/platform-265x50-1.bmp"))
	# Second BigSnail sits here
        self.gameobjects.append(ImageBox(2400,704,265,25,"./pics/platform-265x50-1.bmp"))
        self.gameobjects.append(ImageBox(800,200,265,25,"./pics/platform-265x50-1.bmp"))
        # ladders      
	# first part 
        self.ladders.append(Ladder(1000,200,20,71,"./pics/ladder-toadmanlevel-20x71.bmp"))
	# second part 
        self.ladders.append(Ladder(1000,271,20,71,"./pics/ladder-toadmanlevel-20x71.bmp"))

        
 
    def draw(self,screen,player):
        # draw bg
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        # draw walls
        MaproomDungeon.draw(self,screen)
        for t in self.tileboxes:
            t.draw(screen,self.relativex,self.relativey)
        #self.southwall1.draw(screen,self.relativex,self.relativey)
        # draw gameobjects
        for i in self.gameobjects:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
	for i in self.ladders:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
		
    def isroomdownexit(self):
	if self.relativex < -2370:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomdownexit():
		self.setxyfromdown()
		return 2
	return 0 
 
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single), put enemies before walls in gameobjects
	return None

    def collideswordlow(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithswordlow(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single), put enemies before walls in gameobjects
	return None

    def moveleft(self):
        self.direction = "west"
	self.prevx = self.relativex + 10
	self.prevy = self.relativey
        self.relativex = self.relativex - 10

	#print "move map left %d" % self.relativex
	
### NOTE : the following code does not move a map window to the left,
###	   the player cannot go left

    def moveright(self):
        self.direction = "east"
	self.prevx = self.relativex - 10
	self.prevy = self.relativey
	if self.relativex < 30:
	        self.relativex = self.relativex + 10

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
