from cmu_112_graphics import *
import math

#this file contains the Bird class and the special Bird subclasses
#it also contains the Egg class which Matilda Bird uses

class Bird(object):
    def __init__(self, x, y, dx, dy, gravity, name):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = 21
        self.mass = 6
        self.dragBird = False
        self.drawSling = True
        self.itemsCollided = []
        self.name = name
        self.alive = True
        self.played = False
        self.noGravity = gravity
        self.overlap = False
        self.health = 10000
        self.collided = False

    def __repr__(self):
        return self.name

    def move(self):
        self.x += self.dx
        self.y += self.dy
        #acceleration due to gravity
        #if overlapping with object from below, cancel out gravity
        if (self.drawSling == False and self.noGravity == False and self.overlap == False):
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

    #returns the boundaries of the object
    def getBounds(self):
        top = self.y - self.radius
        bot = self.y + self.radius
        left = self.x - self.radius
        right = self.x + self.radius
        return top, bot, left, right

    def launchProjectile(self, birdX, birdY, slingstartcx, slingstartcy, slingK):
        x = self.distance(birdX, birdY, slingstartcx, slingstartcy)
        elasticEnergy = self.getElasticEnergy(x, slingK)
        #elastic energy in the slingshot transfers to kinetic energy of bird
        initialV = self.getInitialVelocity(elasticEnergy)
        dY = birdY - slingstartcy 
        dX = birdX - slingstartcx
        #calculating the angle based on a reference point and adding 180 degrees to it (fling in the opposite direction)
        angle = math.atan2(dY, dX) + math.pi
        self.dx = initialV * math.cos(angle)
        self.dy = initialV * math.sin(angle)
        self.played = True

    #mv^2/2 = kx^2/2 so v = sqrt((2*Ue)/m)
    def getInitialVelocity(self, kineticEnergy):
        return math.sqrt((2*kineticEnergy)/self.mass)

    #returns elastic energy of the slingshot based on given distance stretched
    def getElasticEnergy(self, distance, k):
        return (1/2) * k * (distance**2)
            
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

    def usePower(self):
        pass

class YellowBird(Bird):
    def __init__(self, x, y, dx, dy, gravity, name):
        super().__init__(x, y, dx, dy, gravity, name)
        self.usedPower = False

    def usePower(self):
        if(self.usedPower == False):
            self.dx *= 4
            self.dy *= 4
            self.usedPower = True

class BigRedBird(Bird):
    def __init__(self, x, y, dx, dy, gravity, name):
        super().__init__(x, y, dx, dy, gravity, name)
        self.mass = 12
        self.radius = 32

class BoomerangBird(Bird):
    def __init__(self, x, y, dx, dy, gravity, name):
        super().__init__(x, y, dx, dy, gravity, name)
        self.radius = 28
        self.dvx = 0
        self.dvy = 0
        self.curved = False
        self.usedPower = False
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if(self.curved):
            if(self.dxInit > 0):
                if(self.dx > 0 or abs(self.dx) <= 20):
                    self.dx += self.dvx
            else:
                if(self.dx < 0 or abs(self.dx) <= 20):
                    self.dx += self.dvx
        self.dy += self.dvy
        #acceleration due to gravity
        #if overlapping with object from below, cancel out gravity
        if (self.drawSling == False and self.noGravity == False and self.overlap == False):
            self.dy += 0.5
        if (self.y + self.radius >= 622):
            self.y = 622 - self.radius
            self.dy = 0
            #friction on the ground
            self.dx = int(self.dx)
            if (self.dx > 0):
                self.dx -= 2
            elif (self.dx < 0):
                self.dx += 2

    def usePower(self):
        if (self.usedPower == False):
            self.curved = True
            self.dxInit = self.dx
            self.dyInit = self.dy
            self.dvx = -3
            self.dvy = 2.5
            self.usedPower = True

class MatildaBird(Bird):
    def __init__(self, x, y, dx, dy, gravity, name):
        super().__init__(x, y, dx, dy, gravity, name)
        self.radius = 29
        self.usedPower = False

    def usePower(self):
        if(self.usedPower == False):
            #launch the bird in a new direction after it releases the egg
            self.dx *= 2
            if (self.dy > 0):
                if (abs(self.dy) <= 2):
                    self.dy *= -9
                elif (abs(self.dy) <= 4):
                    self.dy *= -6
                else:
                    self.dy *= -3
            else:
                if (abs(self.dy) <= 2):
                    self.dy *= 9
                elif (abs(self.dy) <= 4):
                    self.dy *= 6
                else:
                    self.dy *= 3
            self.usedPower = True
            egg = Egg(self.x, self.y + self.radius + 17, True, "MatildaEgg")
            return egg


class Egg(object):
    def __init__(self, x, y, alive, name):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 15
        self.radius = 14
        self.mass = 15
        self.alive = alive
        self.name = name
        self.health = 1000
        self.noGravity = False
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