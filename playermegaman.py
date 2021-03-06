

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
from stateimagelibrary import *
from playerbase import *
from rng import *

class PlayerMegaMan(PlayerBase):
    "Player"
    def __init__(self,heartmeter):
        PlayerBase.__init__(self,heartmeter)
        
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-right-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/megaman-right-2.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/megaman-right-3.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/megaman-right-4.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/megaman-right-5.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/megaman-right-6.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)

        self.stimlibleft = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-left-1.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/megaman-left-2.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/megaman-left-3.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/megaman-left-4.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/megaman-left-5.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/megaman-left-6.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)

        self.stimlibfight = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-right-1.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)

        self.stimlibclimbing = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-climbing-1.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/megaman-climbing-2.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibclimbing.addpicture(image)

        self.stimlibduck = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-right-1.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibduck.addpicture(image)

        self.stimlibhurt = Stateimagelibrary()	
        image = pygame.image.load('./pics/megaman-left-hurt-1.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibhurt.addpicture(image)
        image = pygame.image.load('./pics/megaman-right-hurt-1.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibhurt.addpicture(image)

        self.hitpoints = 20 
        self.duck = 0
        self.jumpcounter = 0

    def hit(self):
	self.heartmeter.index -= 1
	self.hitpoints -= 1
	self.hurt += 1
	if self.heartmeter.index <= 0:
		return 0 #FIXME1 FIX for gameover when collision with enemies 
	else:
		return 1	

    def collidewithenemyweapon(self,room,o):
        # FIXME NOTE
        for o in room.gameobjects:
            
            if o and o.collidewithsword(room,self):
                return self ## NOTE : returns collided entity (single)		
	return None

    def hitwithenemyweapon(self,damage):
	if damage > 0:
		print 'player is hit!'
        self.hitpoints -= damage

    def hitwithenemyweaponlow(self,damage):
	if damage > 0:
		print 'player is hit low!'
        self.hitpoints -= damage

    def pickup(self,room):
        n = room.pickup(self)
	return n

    def fightlow(self,room):
        self.fightcounter = 1
        
        o = room.collideswordlow(self)
        
        if o:
            print "LOW: fight scored hit on %s!" % o
            o.hitwithweapon(self.sword.roll())

    def fightmedium(self,room):
        self.fightcounter = 1
        
        o = room.collidesword(self)
        
        if o:
            print "MEDIUM-HIGH: fight scored hit on %s!" % o
            o.hitwithweapon(self.sword.roll())

    def jump(self, room):
        self.jumpcounter = 20
        self.direction = 'north'

    def update(self,room):
       if self.jumpcounter > 0 and self.jumpcounter < 200:
            room.relativey += 20
            self.jumpcounter += 12
       else:   
            self.jumpcounter = 0
            
    def hitfrombullet(self,hploss):
	1 #kludge so the player can collide with its own bullets
	
    def setrubysword(self):
	self.sword = RubySword(0,0)
