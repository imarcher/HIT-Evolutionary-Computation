from Algorithms import ea1,ea2,ea3
from Individual import Individual
from Population import Population
from TSPProblem import TSPProblem
from Read_data import read_tour

# 200 101 76 70

pop_size = 10
filepath = "data/eil51.tsp"
batch_size = 20000

with open("eil51.txt", 'w') as f:
    with open("eil51_log.txt", 'w') as f2:
        f.write("filepath:%s\n"%filepath)
        f2.write("filepath:%s\n"%filepath)
        for pop_size in (10, 20, 50 ,100):
            f.write("\n")
            f2.write("\n")
            f.write("pop_size:%d\n"%pop_size)
            f2.write("pop_size:%d\n"%pop_size)

            f.write("ans:\n")
            tsp = TSPProblem(filepath)
            
            ans = Individual(TSPProblem(filepath))
            ans.tour = read_tour(tsp.DIMENSION, tsp.ans_tour_path)
            ans.setLength()
            f.write(str(ans.length))
            f.write("\n")

            #test ea1
            f.write("test ea1:")
            f2.write("test ea1:\n")
            log_tour, log_len = ea1(pop_size, filepath, batch_size)
            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")
            i = 1
            for len in log_len:
                f.write("batch_size:%d\n"%(i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1
            
            #test ea2
            f.write("test ea2:")
            f2.write("test ea2:\n")
            log_tour, log_len = ea2(pop_size, filepath, batch_size)
            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")
            i = 1
            for len in log_len:
                f.write("batch_size:%d\n"%(i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1

            #test ea3
            f.write("test ea3:")
            f2.write("test ea3:\n")
            log_tour, log_len = ea3(pop_size, filepath, batch_size)
            for tour in log_tour:
                tour = [str(x) for x in tour]
                s = ' '.join(tour)
                f2.write(s)
                f2.write("\n")
            i = 1
            for len in log_len:
                f.write("batch_size:%d\n"%(i * 5000))
                f.write(str(len))
                f.write("\n")
                i += 1
            print(1)
            f.write("***********************************************")
            f2.write("***********************************************")
