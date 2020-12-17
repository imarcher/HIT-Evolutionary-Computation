from Algorithms import ea1, ea2, ea3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import read_tour
import numpy as np

filelist = ["data/eil51.tsp","data/eil76.tsp","data/eil101.tsp","data/kroA100.tsp","data/kroC100.tsp","data/kroD100.tsp"\
            ,"data/lin105.tsp","data/pcb442.tsp","data/pr2392.tsp","data/st70.tsp"]
with open("opt_tour_ans.txt", 'w') as f:
    for filename in filelist:
        tsp = TSPProblem(filename)
        tsp.get_opt_tour()
        f.write("problem:%s\n" % tsp.NAME)
        ind = Individual(tsp)
        ind.tour = tsp.given_opt_tour
        ind.setLength()
        f.write("length:%f\n" % (ind.length))
        f.write("*********************************************************************\n")



