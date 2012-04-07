#!/opt/local/bin/python

import component
import pygame

################################################################################
################################################################################
################################################################################
class TieBlaster(component.Weapon):
    def __init__(self):
    	component.Weapon.__init__(self)
    	self["range"]=20
	self["damage"]=10
	self["rate"]=10
	self["accuracy"]=25
	self["mass"]=5

    ############################################################################
    def draw(self, ship, surface):
    	here=ship["location"].icoords()
    	pygame.draw.circle(surface, (255,255,255), here, self["range"], 1)

#EOF
