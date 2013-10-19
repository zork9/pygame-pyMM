

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
from random import *

class RNG(Gameobject):
    "Random Number God"
    def __init__(self):
        1

    def rolld6(self):
        return randint(1,6)

    def rolld4(self):
        return randint(1,4)

    def rolld2(self):
        return randint(1,2)

    def rollbroadsword(self):
        if randint(0,3) > 2:
            return 0
        
        r = self.rolld4()
        if r == 4: # critical hit
            return 4*2
        else:
            return r

    def rollgoblinknife(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r

    def rollbullfrog(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r
   
    def rollbeholderbatzap(self):
	if randint(0,4) <= 3:
		return 0

	r = self.rolld2()
	return r

    def rollironknuckle(self):
        if (randint(0,3) == 0):
            return self.rolld4()
        return 0
    
    def rollbeholderzap(self):
	if randint(0,1) == 0:
		return 0

	r = self.rolld4()
	return r
