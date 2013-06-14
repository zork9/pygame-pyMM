
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
from playerkatta import *
from playerfighter import *
from playermagicuser import *
from playerelf import *
from playerdrow import *

class PlayerBase:
    def __init__(self):
        1

class PlayerBase(PlayerBase,PlayerBase):
    "Player"

    PlayerBase.FIGHTER,PlayerBase.MAGICUSER = xrange(2)#,PlayerBase.MAGICUSER,PlayerBase.THIEF = xrange(3)
    PlayerBase.KATTA,PlayerBase.DROW = xrange(2)#,PlayerBase.HUMAN,PlayerBase.DROW = xrange(3)
    
    def __init__(self,PLAYERRACE,PLAYERCLASS,heartmeter):
        classByType = {
                #PlayerBase.HUMAN : PlayerHuman,
                PlayerBase.KATTA : PlayerKatta,
                #PlayerBase.ELF : PlayerElf,
                PlayerBase.DROW : PlayerDrow,
        }
        classByType2 = {
                PlayerBase.FIGHTER : PlayerFighter,
                PlayerBase.MAGICUSER : PlayerMagicUser,
                #Player.THIEF : PlayerThief,
        }
	self.heartmeter = heartmeter
	self.direction = "none"
	self.prevdirection = "right"
        self.x = 280 
        self.y = 300 
        self.w = 50 
        self.h = 50 
#	self.stimlib = Stateimagelibrary()	
#        image = pygame.image.load('./pics/player1-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player3-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player1-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	
#        image = pygame.image.load('./pics/player3-30x30.bmp').convert()
#        image.set_colorkey((0,0,0)) 
#	self.stimlib.addpicture(image)	

#        self.stimlibfight = Stateimagelibrary()	
#        image = pygame.image.load('./pics/playerfight1-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)
#        image = pygame.image.load('./pics/playerfight1-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)
#        image = pygame.image.load('./pics/playerfight2-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)
#        image = pygame.image.load('./pics/playerfight2-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)
#        image = pygame.image.load('./pics/playerfight3-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)
#        image = pygame.image.load('./pics/playerfight3-30x30.bmp').convert()
#        image.set_colorkey((0,0,0))
#        self.stimlibfight.addpicture(image)

        self.fightcounter = 0

###        classByType[PLAYERRACE](heartmeter)
###        classByType2[PLAYERCLASS](heartmeter)

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

    def drawduck(self, screen):
	self.stimlibduck.draw(screen,self.x,self.y)
	
    def draw(self, screen):
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

        
    def hit(self):
	self.heartmeter.index -= 1 
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

