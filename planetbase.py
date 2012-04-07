#!/opt/local/bin/python

import math
from ship import Ship
from tieEngine import TieEngine
from zapper import Zapper
from tiePowerSupply import TiePowerSupply
from fighterHull import FighterHull
from shield import Shield

################################################################################
################################################################################
################################################################################
class PlanetBase(Ship):
    def __init__(self, **kwargs):
	Ship.__init__(self, **kwargs)
	self["hits"]=1000000
	self["radius"]=10
	self["color"]=(0,0,255)

    ############################################################################
    def steer(self):
    	pass

    ############################################################################
    def move(self):
    	pass

    ############################################################################
    def getAcceleration(self):
    	self["acc"]=0

    ############################################################################
    def attack(self):
    	pass

#EOF
