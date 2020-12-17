import numpy as np
import random
import numpy as np
import math
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import read_tour
#pmx_crossover+swap_mutation+tournament_selection
#pop_size: number of inds
#path: the file path
#batch_size: how many generations
#bad result
def ea1(pop_size,path,batch_size):
    mutation_possiblity = 6
    tsp = TSPProblem(path)
    pop = Population(pop_size, tsp)
    #ini
    pop.ini_tourlist()
    pop.set_length()
    pop.get_adaptability()

    log_tour = []
    log_len = []

    for i in range(batch_size):

        #option parents 1/3
        parents_pop = pop.tournament_selection(int(pop.size/3),3)

        #cross random from parents
        child_list = []
        while len(child_list) != pop_size:
            parent1 = random.randint(0, parents_pop.size - 1)
            parent2 = random.randint(0, parents_pop.size - 1)
            parent1 = parents_pop.tourlist[parent1]
            parent2 = parents_pop.tourlist[parent2]
            #cross
            child1,child2 = parents_pop.pmx_crossover(parent1,parent2)
            child_list.append(child1)
            child_list.append(child2)


        for j in range(pop_size):
            rate = random.randint(1,10)
            # mutation
            if rate <= mutation_possiblity:
                pop.swap_mutation(child_list[j])

        #make the chlid population
        pop = Population(pop_size,tsp)
        pop.tourlist = child_list
        pop.set_length()
        pop.get_adaptability()

        if i%100 == 0:
            min_len = pop.tourlist[0].length
            min_num = 0
            for j in range(1,pop_size):
                if pop.tourlist[j].length < min_len:
                    min_len = pop.tourlist[j].length
                    min_num = j
            log_tour += [pop.tourlist[min_num].tour]
            if i % 5000 == 0:
                log_len += [min_len]

    return log_tour, log_len

#order crossover+scramble_mutation+elitism_selection
#better result
def ea2(pop_size,path,batch_size):
    mutation_possiblity = 6
    tsp = TSPProblem(path)
    pop = Population(pop_size, tsp)
    #ini
    pop.ini_tourlist()
    pop.set_length()
    pop.get_adaptability()

    log_tour = []
    log_len = []

    for i in range(batch_size):
        #option parents 1/3
        parents_list = pop.elitism_selection(int(pop.size/3))
        parents_pop = Population(int(pop.size/3),tsp)
        parents_pop.tourlist = parents_list

        #cross random from parents
        if len(parents_list)%2 == 0:
            child_list = parents_list
        else:
            child_list = parents_list[0:len(parents_list)-1]

        while len(child_list) != pop_size:
            parent1 = random.randint(0, parents_pop.size - 1)
            parent2 = random.randint(0, parents_pop.size - 1)
            parent1 = parents_pop.tourlist[parent1]
            parent2 = parents_pop.tourlist[parent2]
            #cross
            child1,child2 = parents_pop.order_crossover(parent1,parent2)
            child_list.append(child1)
            child_list.append(child2)


        for j in range(pop_size):
            rate = random.randint(1,10)
            # mutation
            if rate <= mutation_possiblity:
                pop.scramble_mutation(child_list[j])

        #make the chlid population
        pop = Population(pop_size,tsp)
        pop.tourlist = child_list
        pop.set_length()
        pop.get_adaptability()

        if i%100 == 0:
            min_len = pop.tourlist[0].length
            min_num = 0
            for j in range(1,pop_size):
                if pop.tourlist[j].length < min_len:
                    min_len = pop.tourlist[j].length
                    min_num = j
            log_tour += [pop.tourlist[min_num].tour]
            if i % 5000 == 0:
                log_len += [min_len]

    return log_tour, log_len

#order crossover+inversion_mutation+elitism_selection
#best result
def ea3(pop_size,path,batch_size):
    mutation_possiblity = 6
    tsp = TSPProblem(path)
    pop = Population(pop_size, tsp)
    #ini
    pop.ini_tourlist()
    pop.set_length()
    pop.get_adaptability()

    log_tour = []
    log_len = []

    for i in range(batch_size):
        #option parents 1/3
        parents_list = pop.elitism_selection(int(pop.size/3))
        parents_pop = Population(int(pop.size/3),tsp)
        parents_pop.tourlist = parents_list

        #cross random from parents
        if len(parents_list)%2 == 0:
            child_list = parents_list
        else:
            child_list = parents_list[0:len(parents_list)-1]

        while len(child_list) != pop_size:
            parent1 = random.randint(0, parents_pop.size - 1)
            parent2 = random.randint(0, parents_pop.size - 1)
            parent1 = parents_pop.tourlist[parent1]
            parent2 = parents_pop.tourlist[parent2]
            #cross
            child1,child2 = parents_pop.order_crossover(parent1,parent2)
            child_list.append(child1)
            child_list.append(child2)


        for j in range(pop_size):
            rate = random.randint(1,10)
            # mutation
            if rate <= mutation_possiblity:
                pop.inversion_mutation(child_list[j])

        #make the chlid population
        pop = Population(pop_size,tsp)
        pop.tourlist = child_list
        pop.set_length()
        pop.get_adaptability()

        if i%100 == 0:
            min_len = pop.tourlist[0].length
            min_num = 0
            for j in range(1,pop_size):
                if pop.tourlist[j].length < min_len:
                    min_len = pop.tourlist[j].length
                    min_num = j
            log_tour += [pop.tourlist[min_num].tour]
            if i % 5000 == 0:
                log_len += [min_len]

    return log_tour, log_len

