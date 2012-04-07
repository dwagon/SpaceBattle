import math

################################################################################
class Coord:
    def __init__(self, x, y):
    	self.x=x
	self.y=y

    ############################################################################
    def coords(self):
    	return (self.x, self.y)

    ############################################################################
    def icoords(self):
    	return (int(self.x), int(self.y))

    ############################################################################
    def displace(self, distance, angle):
    	deltax=math.cos(angle)*distance
	deltay=math.sin(angle)*distance
    	return Coord(self.x+deltax, self.y+deltay)

    ############################################################################
    def __ne__(self, loc):
    	return (self.x!=loc.x or self.y!=loc.y)

    ############################################################################
    def __eq__(self, loc):
    	return (self.x==loc.x and self.y==loc.y)

    ############################################################################
    def __nonzero__(self):
    	return self.x!=0 or self.y!=0

    ############################################################################
    def maxsize(self, width, height):
    	if self.x<0:
	    self.x=0
	if self.y<0:
	    self.y=0
	if self.x>width:
	    self.x=width
	if self.y>height:
	    self.y=height

    ############################################################################
    def distance(self, loc):
	dist=math.sqrt((self.x-loc.x)**2 + (self.y-loc.y)**2)
	return dist

    ############################################################################
    def box(self, length):
    	half=length/2.0
    	return (Coord(self.x-half, self.y-half), Coord(self.x+half, self.y+half))

    ############################################################################
    def angle(self, other):
    	return math.atan2(other.y-self.y, other.x-self.x)

    ############################################################################
    def inside(self, box):
    	tl=box[0]
	br=box[1]
	if tl.x<self.x<br.x and tl.y<self.y<br.y:
	    return True
	return False

    ############################################################################
    def __repr__(self):
    	return "<%d, %d>" % (self.x,self.y)

#EOF
