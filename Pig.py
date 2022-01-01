from cmu_112_graphics import *
import math

#this file contains the pig class

class Pig(object):
    def __init__(self, x, y, dx, dy, gravity, name):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = 24
        self.mass = 4
        self.alive = True
        self.collideBird = False
        self.name = name
        self.fullHealth = 300
        self.health = 300
        self.itemsCollided = []
        self.noGravity = gravity
        self.overlap = False

    def __repr__(self):
        return self.name

    def move(self):
        self.x += self.dx
        self.y += self.dy
        #acceleration due to gravity
        if (self.noGravity == False and self.overlap == False):
            self.dy += 0.5
        if (self.y + self.radius >= 622):
            self.y = 622 - self.radius
            self.dy = 0
            #friction on the ground
            self.dx = int(self.dx)
            if (self.dx > 0):
                self.dx -= 1
            elif (self.dx < 0):
                self.dx += 1
        #if pig goes too far near the slingshot make it stop there
        if (self.x <= 300):
            self.x = 300
        #if pig goes off boundary then it dies
        #screen boundaries is 1280, 720
        if (self.x > 1280 or self.x < 0 or self.y < 0):
            self.alive = False

    #returns the boundaries of the object
    def getBounds(self):
        top = self.y - self.radius
        bot = self.y + self.radius
        left = self.x - self.radius
        right = self.x + self.radius
        return top, bot, left, right

    #returns final velocity of self in x direction after collision
    def getvxf(self, other):
        # vaf|cm = -vai|cm
        # vaf - vcm = -(vai - vcm)
        # vaf = -vai + 2vcm 
        vxf = -(self.dx) + 2*(self.getvcmx(other))
        return vxf

    #returns final velocity of self in y direction after collision
    def getvyf(self, other):
        # vaf|cm = -vai|cm
        # vaf - vcm = -(vai - vcm)
        # vaf = -vai + 2vcm 
        vyf = -(self.dy) + 2*(self.getvcmy(other))
        return vyf

    #returns velocity of center of mass of two objects in x direction
    def getvcmx(self, other):
        return ((self.getpx() + other.getpx()) / (self.mass + other.mass))

    #returns velocity of center of mass of two objects in y direction
    def getvcmy(self, other):
        return ((self.getpy() + other.getpy()) / (self.mass + other.mass))

    #returns momentum of bird in the x direction
    def getpx(self):
        return self.dx * self.mass

    #returns momentum of bird in the y direction
    def getpy(self):
        return self.dy * self.mass
            
    #returns the distance between two points
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    #returns the angle beginning from the coordinates of xref, yref to x, y
    def getAngle(xref, yref, x, y):
        dY = yref - y
        dX = xref - x
        #calculating the angle based on a reference point
        angle = math.atan2(dY, dX)
        return angle