import random
import numpy as np
import math

# a possible solution
class Individual:
    def __init__(self, tsp):
        # number of city
        self.dimension = tsp.DIMENSION
        # position of city,0 - n-1
        self.pos = tsp.POS
        # the path of this solution , 0 - n-1
        self.tour = []
        # length of tour
        self.length = 0
        #
        self.adaptability = 0

    # use for sort
    def __lt__(self, other):
        if self.adaptability < other.adaptability:
            return True
        return False

    # ini tour randomly with certain first one
    def setTour(self):
        while len(self.tour) != self.dimension:
            next = random.randint(0, self.dimension-1)
            if next not in self.tour:
                self.tour.append(next)

    # compute the length of this tour
    def setLength(self):
        self.length = 0
        for i in range(self.dimension - 1):
            cityone = self.pos[int(self.tour[i])-1]
            citytwo = self.pos[int(self.tour[i + 1])-1]
            x1 = cityone[1]
            y1 = cityone[2]
            x2 = citytwo[1]
            y2 = citytwo[2]
            self.length = self.length + math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

    def print_tour(self):
        #print("tour:",self.tour)
        print("length",self.length)

