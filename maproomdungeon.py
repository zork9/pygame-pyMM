

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
from time import *
from maproom import *
from wall import *

class MaproomDungeon(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.northwalls = []
        self.southwalls = []
        self.westwalls = []
        self.eastwalls= []
        self.gameobjects = []
        self.tileboxes = []
        self.pits = []
        self.ropes = []
        self.ladders = []
	self.bullets = []
        
    def addnorthwall(self, x,y,w,h,imagefilename):
        self.northwalls.append(Wall(x,y,w,h,imagefilename))

    def addsouthwall(self, x,y,w,h,imagefilename):
        self.southwalls.append(Wall(x,y,w,h,imagefilename))

    def addwestwall(self, x,y,w,h,imagefilename):
        self.westwalls.append(Wall(x,y,w,h,imagefilename))

    def addeastwall(self, x,y,w,h,imagefilename):
        self.eastwalls.append(Wall(x,y,w,h,imagefilename))
        
    def draw(self,screen):
	##print "x=%d" % self.relativex 
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for w in self.northwalls:
            w.draw(screen,self)
        for w in self.southwalls:
            w.draw(screen,self)
        for w in self.westwalls:
            w.draw(screen,self)
        for w in self.eastwalls:
            w.draw(screen,self)

    def collidewithladders(self, player):	
	for i in self.ladders:
	    if i != None and i.collidewithladder(self, player):
		return 2
	return 0

    def collidewithladdersdown(self, player):	
	for i in self.ladders:
	    if i != None and i.collidewithladderdown(self, player):
		return 2
	return 0

      
      
# NOTE player can be enemy 
    def collide(self, player,hploss):	
	for i in self.gameobjects:
	    #print "go> %s" % i
	    if i != None and i.collide(self,player,hploss): ### NOTE hp loss of hploss
		return 2 # 1 kills game
	for i in self.northwalls:
	    if i != None and i.collide(self,player,hploss):
		return 2
	for i in self.southwalls:
	    if i != None and i.collide(self,player,hploss):
		return 2
	for i in self.westwalls:
	    if i != None and i.collide(self,player,hploss):
		return 2
	for i in self.eastwalls:
	    if i != None and i.collide(self,player,hploss):
		return 2
#	for i in self.tileboxes:
#		if i != None and i.collide(self,player,hploss):
#			#self.undomove()
#	                # FIXME self.undomove()
#			return 2 
#	for i in self.pits:
#		if i != None and i.collide(self,player,hploss):
#			return 2
	return 0

    def collidewithenemy(self, enemy):
	for t in self.tileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
        return 0


    def fall(self, player):
        self.moveup()
        for i in self.gameobjects:
	    if i != None and i.fallcollide(self, player):
                self.movedown()
		return 2 # 1 kills game
        
        return 0
