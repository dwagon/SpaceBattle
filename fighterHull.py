#!/opt/local/bin/python

import component

class FighterHull(component.Hull):
    def __init__(self):
	component.Hull.__init__(self)
	self["maxspace"]=10
	self["maxmass"]=1000

#EOF
