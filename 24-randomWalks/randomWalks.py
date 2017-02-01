"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:52 2017
Number of code lines: 
82
"""
import random

class Location():
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def move(self,deltaX,deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return (str(self.x) + ',' + str(self.y))


class Field():
    def __init__(self):
        self.drunks = {}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist,yDist)

    def getLoc(self,drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk():
    def __init__(self, name):
        self.name = name

    def takeStep(self):
        stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
        return random.choice(stepChoices)

    def __str__(self):
        return "This drunk is nammed " + self.name


def walk(f,d,numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer,origin)
        distances.append(walk(f,homer,numSteps))
    return distances

def drunkTest(numTrials):
    for numSteps in [0,1, 10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print("Random walk of {} steps, Mean : {} , Max : {} , Min : {}".format(numSteps,sum(distances)/len(distances),
                                                                                max(distances), min(distances)))
drunkTest(10)
