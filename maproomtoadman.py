
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
from imagebox import *
from skeletondrone import *
from greenscorpion import *
from rainman import *
from bombertoad import *
from toadman import *

class MaproomToadMan(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/bgtoadman-640x600.bmp').convert()

	self.w = 640
	self.h = 480

	self.mapoffsetx = 400

        self.gameobjects.append(ToadMan(400,420))
        
        # left NOTE : boxes collide so put them after enemies !
        self.gameobjects.append(Box(0,400,640,250))
        self.gameobjects.append(ImageBox(0,0,640,50,"./pics/platform-265x50-1.bmp"))
	### walls 
        self.addwestwall(0,0,50,480,"./pics/wall-level1-1.bmp")
        self.addeastwall(590,0,50,480,"./pics/wall-level1-1.bmp")
        
 
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
	for i in self.ropes:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
		
    def isroomdownexit(self):
	if self.relativex  < -250 and self.relativex > -650 and self.relativey < -650:
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

    def moveright(self):
        self.direction = "east"
	self.prevx = self.relativex - 10
	self.prevy = self.relativey
        self.relativex = self.relativex + 10

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
