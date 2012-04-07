#!/opt/local/bin/python

import math
from ship import Ship
from tieEngine import TieEngine
from tieBlaster import TieBlaster
from tiePowerSupply import TiePowerSupply
from fighterHull import FighterHull

################################################################################
################################################################################
################################################################################
class TieFighter(Ship):
    def __init__(self, **kwargs):
	imagefile="data/tiefighter.png"
	Ship.__init__(self, **kwargs)
	self.hull=FighterHull()
	self["hits"]=100
	self.addComponent(TieEngine())
	self.addComponent(TieEngine())
	self.addComponent(TieBlaster())
	self.addComponent(TieBlaster())
	self.addComponent(TiePowerSupply())
	self["agility"]=math.radians(5)
	self["color"]=(0,255,0)

    ############################################################################
    def steer(self):
    	""" Try and hook up with friends before attacking enemies
	"""
	enemy=self.closest_enemy()
    	friend=self.closest_friend()

	if enemy and self.distance(enemy)<20:
	    self["mode"]="Psycho"
	    target=enemy
	elif friend and self.distance(friend)>20:
	    self["mode"]="Chum hunt"
	    target=friend
	else:
	    self["mode"]="Scum hunt"
	    target=enemy
	self.move_towards(target)

################################################################################
if __name__=="__main__":
    t=TieFighter(name="zoom")
    print t
    for c in t.components:
	print c
    t.validate()
    print "Mass=%s" % t.getMass()
    print "Acc=%s" % t.getAcceleration()
    print "Force=%s" % t.getForce()

#EOF
