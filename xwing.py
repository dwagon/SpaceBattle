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
class XWing(Ship):
    def __init__(self, **kwargs):
	Ship.__init__(self, **kwargs)
	self.hull=FighterHull()
	self.addComponent(TieEngine())
	self.addComponent(TieEngine())
	self.addComponent(Zapper())
	self.addComponent(Zapper())
	self.addComponent(Zapper())
	self.addComponent(Zapper())
	self.addComponent(Shield())
	self.addComponent(TiePowerSupply())
	self["hits"]=100
	self["agility"]=math.radians(1)
	self["color"]=(255,0,0)

    ############################################################################
    def steer(self):
    	if self["hits"]<75:
	    self["mode"]="Runaway"
	    neutral=self.closest_neutral()
	    newdir=self["location"].angle(neutral["location"])	
	    self.steer_towards(newdir)
    	else:
	    closest=self.closest_enemy()
	    if self.distance(closest)>10:
		self.move_towards(closest)
		self["mode"]="Attack"
	    else:
		newdir=math.pi+self["location"].angle(closest["location"])	
		self["mode"]="Back off"
		self.steer_towards(newdir)

################################################################################
if __name__=="__main__":
    x=XWing()
    print x
    for c in x.components:
	print c
    x.validate()
    print "Mass=%s" % x.getMass()
    print "Acc=%s" % x.getAcceleration()
    print "Force=%s" % x.getForce()

#EOF
