#!/opt/local/bin/python

import pygame
import random
import coord, base

################################################################################
################################################################################
################################################################################
class Space(base.BaseClass):
    def __init__(self, **kwargs):
    	self.ships=[]
	self.data={
	    'width': 640,
	    'height': 480,
	    'screen': None,
	    }
	self.data.update(kwargs)

    ############################################################################
    def draw(self):
	for ship in self.ships:
	    ship.draw(self["screen"])

    ############################################################################
    def addShip(self, shipClass, **kwargs):
    	if 'location' not in kwargs:
	    l=coord.Coord(random.randrange(self["width"]), random.randrange(self["height"]))
	    kwargs['location']=l
    	ship=shipClass(**kwargs)
	ship.init(screen=self["screen"])
    	self.ships.append(ship)

    ############################################################################
    def turn(self):
    	for ship in self.ships:
	    ship.turn()
	
	sides=set()
	for ship in self.ships[:]:
	    if ship["hits"]<=0:
	    	print "%s goes boom!" % ship["name"]
	    	self.ships.remove(ship)
	    else:
	    	if ship["side"]:
		    sides.add(ship["side"])

	if len(sides)==1:
	    print "One side left"
	    return True
	return False

    ############################################################################
    def shipList(self):
    	print "ShipList"
    	for s in self.ships:
	    print s

    ############################################################################
    def initShips(self):
    	from tie_fighter import TieFighter
    	from xwing import XWing
	from planetbase import PlanetBase
	self.addShip(TieFighter, name="tie1", side="E")
	self.addShip(TieFighter, name="tie2", side="E")
	self.addShip(TieFighter, name="tie3", side="E")
	self.addShip(TieFighter, name="tie4", side="E")
	self.addShip(XWing, name="xwing1", side="R")
	self.addShip(XWing, name="xwing2", side="R")
	#self.addShip(XWing, name="xwing3", side="R")
	#self.addShip(XWing, name="xwing4", side="R")
	self.addShip(PlanetBase, name="planet", location=coord.Coord(self["width"]/2, self["height"]/2), side="")

	for ship in self.ships:
	    ship.space=self

#EOF
