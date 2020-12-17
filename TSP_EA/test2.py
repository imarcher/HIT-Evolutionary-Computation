from Algorithms import ea1,ea2,ea3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import read_tour
import numpy as np

# 200 101 76 70

n = 10
pop_size = 50
filepath = "data/eil51.tsp"
batch_size = 10000

with open("eil51_ave.txt", 'w') as f:
    with open("eil51_log_ave.txt", 'w') as f2:
        f.write("filepath:%s\n"%filepath)
        f2.write("filepath:%s\n"%filepath)
        lens = []
        for t in range(n):
            f.write("\n%d\n"%t)
            f2.write("\n%d\n"%t)

            f.write("ans:\n")
            tsp = TSPProblem(filepath)

            #test ea3
            f.write("average ea3:\n")
            f2.write("average ea3:\n")
            log_tour, log_len = ea3(pop_size, filepath, batch_size)
            
            for tour in log_tour:
                tour_new = [str(x) for x in tour]
                s = ' '.join(tour_new)
                f2.write(s)
                f2.write("\n")
            
            f.write("batch_size:%d\n"%(10000))
            f.write(str(log_len[1]))
            f.write("\n")
            f.write("***********************************************")
            f2.write("***********************************************")
            lens += [log_len[1]]
        
        mean = np.mean(lens)
        std = np.std(lens, ddof = 1)
        f.write("average cost:%f\n"%(mean))
        f.write("standard deviation:%f\n"%(std))

