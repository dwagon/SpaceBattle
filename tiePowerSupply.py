#!/opt/local/bin/python

import component

class TiePowerSupply(component.PowerSupply):
    def __init__(self):
    	component.PowerSupply.__init__(self)
	self["power"]=100
	self["mass"]=10

#EOF
