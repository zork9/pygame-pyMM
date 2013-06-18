
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

class Wall(Gameobject):
    ""
    def __init__(self, xx,yy,ww,hh,filename):
        Gameobject.__init__(self,xx,yy)
        self.w = ww 
        self.h = hh
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0,0,0)) 
    
    def draw(self, screen, room):
        screen.blit(self.image, (self.x+room.relativex,self.y+room.relativey))

    def collide(self, room, player, hploss):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Wall! x=%d y=%d" % (room.relativex,room.relativey) 
	    return 3 # NOTE return 3 for dungeon wall
	else:
	    return 0

