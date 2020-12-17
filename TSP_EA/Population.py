import random
import numpy as np
import math
from Individual import Individual

# 根据值找到对应下标
def find_index(tour, city):
    for i in range(0, len(tour)):
        if city == tour[i]:
            return i
#use for sort


class Population:

    def __init__(self, size, tsp):
        # the tours of population
        self.tourlist = []
        # the number of tours in population
        self.size = size
        self.dimension = tsp.DIMENSION
        self.tsp = tsp


    def ini_tourlist(self):
        for i in range(self.size):
            ind = Individual(self.tsp)
            ind.setTour()
            self.tourlist.append(ind)

    #compute length
    def set_length(self):
        for ind in self.tourlist:
            ind.setLength()

    # compute adaptability and normalization(0 - 1 float,bigger is better)
    def get_adaptability(self):
        ind_list = self.tourlist
        a = []
        min = ind_list[0].length
        max = min
        for ind in ind_list:
            tmp = ind.length
            a.append(tmp)
            if (tmp < min):
                min = tmp
            if (tmp > max):
                max = tmp
            ind.adaptability = tmp
        for ind in ind_list:
            if(max != min):
                ind.adaptability = 1 - ind.length / max
            else:
                ind.adaptability = 0.5

    # crossover operators
    # order crossover
    def order_crossover(self, parent1, parent2):
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)

        # Choose an arbitrary part from the  parent
        gstart = random.randint(0, self.dimension - 2)
        gend = random.randint(gstart + 1, self.dimension - 1)

        #child1
        gene1 = parent1.tour[gstart: gend+1]
        i = 0
        #Copy the numbers that are not in the first part, to the first child
        while len(child1.tour) < gstart:
            if parent2.tour[i] not in gene1:
                child1.tour.append(parent2.tour[i])
                i = i + 1
            else:
                i = i + 1
        # Copy this part to the first child

        for j in range(gend+1-gstart):
            child1.tour.append(gene1[j])
        # Copy the numbers that are not in the first part, to the first child
        while len(child1.tour) < self.dimension:
            if parent2.tour[i] not in gene1:
                child1.tour.append(parent2.tour[i])
                i = i + 1
            else:
                i = i + 1


        # copy the process front to make the child2
        gene2 = parent2.tour[gstart: gend+1]
        i = 0
        # Copy the numbers that are not in the first part, to the first child
        while len(child2.tour) < gstart:
            if parent1.tour[i] not in gene2:
                child2.tour.append(parent1.tour[i])
                i = i + 1
            else:
                i = i + 1
        # Copy this part to the first child
        for j in range(gend + 1 - gstart):
            child2.tour.append(gene2[j])
        # Copy the numbers that are not in the first part, to the first child
        while len(child2.tour) < self.dimension:
            if parent1.tour[i] not in gene2:
                child2.tour.append(parent1.tour[i])
                i = i + 1
            else:
                i = i + 1

        return child1, child2

    # PMX crossover
    def pmx_crossover(self, parent1, parent2):
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)
        child1.tour = parent1.tour
        child2.tour = parent2.tour
        # Choose an arbitrary part from the  parent
        gstart = random.randint(0, self.dimension - 2)
        gend = random.randint(gstart + 1, self.dimension - 1)
        gene1 = parent1.tour[gstart: gend+1]
        gene2 = parent2.tour[gstart: gend+1]

        # change form
        dic1 = {}
        dic2 = {}
        for i in range(gend + 1 - gstart):
            dic1[gene2[i]] = gene1[i]
            dic2[gene1[i]] = gene2[i]

        # change gene
        child1.tour[gstart: gend+1] = gene2
        child2.tour[gstart: gend+1] = gene1

        # child1
        # place according to the form
        for i in range(gstart):
            while child1.tour[i] in dic1.keys():
                child1.tour[i] = dic1[child1.tour[i]]

        for i in range(gend+1,self.dimension):
            while child1.tour[i] in dic1.keys():
                child1.tour[i] = dic1[child1.tour[i]]


        # child1
        # place according to the form
        for i in range(gstart):
            while child2.tour[i] in dic2.keys():
                child2.tour[i] = dic2[child2.tour[i]]

        for i in range(gend + 1, self.dimension):
            while child2.tour[i] in dic2.keys():
                child2.tour[i] = dic2[child2.tour[i]]

        return child1,child2

    # cycle crossover
    def cycle_crossover(self, parent1, parent2):
        child1 = Individual(self.tsp)
        child2 = Individual(self.tsp)
        child1.tour = parent2.tour
        child2.tour = parent1.tour
        start = random.randint(0, self.dimension - 1)
        startgene = parent1.tour[start]
        #position in tour
        now = start
        nextgene = parent2.tour[now]
        #the positions of cycle citys in tour
        cyc = []
        cyc.append(now)
        #Make a cycle of alleles from P1
        while nextgene != startgene:
            now = find_index(parent1.tour,nextgene)
            cyc.append(now)
            nextgene = parent2.tour[now]

        #child1,2,input the cycle citys
        for i in range(len(cyc)):
            child1.tour[cyc[i]] = parent1.tour[cyc[i]]
            child2.tour[cyc[i]] = parent2.tour[cyc[i]]
        return child1,child2

    # mutation operators
    # insert
    def insert_mutation(self, ind):
        # select two positions on the chromosome at random, and interchange the values
        gene1 = 0
        gene2 = 0
        # prevent gene1 and gene2 are same
        while gene1 == gene2:
            gene1 = random.randint(0, self.dimension - 1)
            gene2 = random.randint(0, self.dimension - 1)
        # insert the last to the front
        if gene1 < gene2:
            ind.tour.insert(gene1+1, ind.tour[gene2])
            ind.tour.pop(gene2+1)
        else:
            ind.tour.insert(gene2+1, ind.tour[gene1])
            ind.tour.pop(gene1+1)
        return ind

    # swap
    def swap_mutation(self, ind):

        # select two positions on the chromosome at random, and interchange the values
        gene1 = 0
        gene2 = 0
        # prevent gene1 and gene2 are same
        while gene1 == gene2:
            gene1 = random.randint(0, self.dimension-1)
            gene2 = random.randint(0, self.dimension-1)
        #interchange the values
        tmp = ind.tour[gene1]
        ind.tour[gene1] = ind.tour[gene2]
        ind.tour[gene2] = tmp
        return ind

    # inversion
    def inversion_mutation(self, ind):
        # select a subset of genes like in scramble mutation
        gstart = random.randint(0, self.dimension - 2)
        gend = random.randint(gstart + 1, self.dimension - 1)
        gene = ind.tour[gstart: gend+1]
        # instead of shuffling the subset
        gene.reverse()
        ind.tour[gstart: gend+1] = gene
        return ind

    # scramble
    def scramble_mutation(self, ind):
        # select a subset of genes like in scramble mutation
        gstart = random.randint(0, self.dimension - 2)
        gend = random.randint(gstart + 1, self.dimension - 1)
        gene = ind.tour[gstart: gend+1]
        # values are scrambled or shuffled randomly
        random.shuffle(gene)
        ind.tour[gstart: gend+1] = gene
        return ind


    # selection methods


    #every individual can become a parent with a probability which is proportional to its fitness
    # p = adapi / sum(adapi)
    # n is number of child
    # return pop
    def fitness_proportional_selection(self, n):
        new_tourlist = self.tourlist[0:n]
        adap_sum = 0
        p = []
        for ind in self.tourlist:
            adap_sum = adap_sum + ind.adaptability
        for i in range(self.size):

            p.append(self.tourlist[i].adaptability / adap_sum *100)
        for i in range(n,self.size):
            rate = random.randint(1, 100)
            #input
            if p[i]>rate:
                find = 0
                while find ==0 :
                    input_pos = random.randint(0, n-1)
                    out_rate = random.randint(1, 100)
                    if new_tourlist[input_pos].adaptability / adap_sum * 100 > out_rate:
                        continue
                    else:
                        find=1
                        new_tourlist[input_pos] = self.tourlist[i]

        childpop = Population(len(new_tourlist),self.tsp)
        childpop.tourlist = new_tourlist
        return childpop

    #Pick k members at random then select the best of these
    # repeat n
    # n is number of child
    #return pop
    def tournament_selection(self, n, k):
        new_tourlist = []
        while len(new_tourlist) != n:
            ktour = []
            while len(ktour) != k :
                r = random.randint(0, self.size-1)
                if self.tourlist[r] not in ktour:
                    ktour.append(self.tourlist[r])
            ktour.sort(reverse=True)
            for i in range(k):
                if ktour[i] not in new_tourlist:
                    new_tourlist.append(ktour[i])
                    break
        childpop = Population(len(new_tourlist), self.tsp)
        childpop.tourlist = new_tourlist
        return childpop

    # n is number of elitism
    #opt the biggest n of the parent
    #return list
    def elitism_selection(self, n):
        self.tourlist.sort(reverse=True)
        elitism_list = self.tourlist[0:n]
        return elitism_list



