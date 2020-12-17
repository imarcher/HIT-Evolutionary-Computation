import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from Read_data import read_data,read_tour


class TSPProblem:

    def __init__(self, path):
        infolist = read_data(path)
        # NAME: data file name
        self.NAME = infolist[0]
        # COMMENT: some information for the data
        self.COMMENT = infolist[1]
        # TYPE: the data type , TSP
        self.TYPE = infolist[2]
        # DIMENSION: the number of the citys
        self.DIMENSION = infolist[3]
        # EDGE WEIGHT TYPE: the implement of the edge weights,EUC_2D
        self.EDGE_WEIGHT_TYPE = infolist[4]
        # POS: position of citys
        self.POS = infolist[5]
        #ans_tour_path: the filepath of opt_tour
        self.ans_tour_path = 'opt_tour/' + self.NAME + '.opt.tour'
    # print info of problem
    def print_info(self):
        print("NAME:",self.NAME)
        print("COMMENT:", self.COMMENT)
        print("TYPE:", self.TYPE)
        print("DIMENSION:", self.DIMENSION)
        print("EDGE_WEIGHT_TYPE:", self.EDGE_WEIGHT_TYPE)
        print("POS:",self.POS)


    def plot(self, route):
        # route为点序列，表示依次连接的点

        figure, ax = plt.subplots()
        # 标点
        for i in range(self.DIMENSION):
            x = self.POS[i][1]
            y = self.POS[i][2]
            ax.scatter(x, y, c='r', s=20, alpha=0.5)

        # 连线
        s = int(route[0])
        source_dot = [self.POS[s-1][1], self.POS[s-1][2]]

        for j in range(self.DIMENSION - 1):
            a = int(route[j + 1] - 1)
            target_dot = [self.POS[a][1], self.POS[a][2]]
            ax.add_line(Line2D([source_dot[0], target_dot[0]], [source_dot[1], target_dot[1]], linewidth=1, color='blue'))
            source_dot = target_dot

        plt.plot()
        plt.show()

    # get the answer of opt_tour
    def get_opt_tour(self):
        opt_tour_path = 'opt_tour/'+ self.NAME +'.opt.tour'
        self.given_opt_tour = read_tour(self.DIMENSION,opt_tour_path)


#a = TSPProblem("data/eil51.tsp")
#a.print_info()
#a.get_opt_tour()


