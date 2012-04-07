#!/opt/local/bin/python

import component
import pygame

################################################################################
################################################################################
################################################################################
class Zapper(component.Weapon):
    def __init__(self):
    	component.Weapon.__init__(self)
    	self["range"]=40
	self["rate"]=50
	self["accuracy"]=50
	self["damage"]=10
	self["mass"]=10

    ############################################################################
    def draw(self, ship, surface):
    	here=ship["location"].icoords()
    	pygame.draw.circle(surface, (255,255,255), here, self["range"], 1)

#EOF
