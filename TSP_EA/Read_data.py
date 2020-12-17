import re
import numpy as np


def read_data(path):
    with open(path,"r") as f:
        name = re.split(r'NAME : |\n', f.readline())[1]
        comment = re.split(r'COMMENT : |\n', f.readline())[1]
        _type = re.split(r'TYPE : |\n', f.readline())[1]
        dimension = int(re.split(r'DIMENSION : |\n', f.readline())[1])
        edge_weight_type = re.split(r'EDGE_WEIGHT_TYPE : |\n', f.readline())[1]
        f.readline()
        #print(name, comment, _type, dimension, edge_weight_type)
        pos = np.zeros((dimension, 3))
        for i in range(dimension):
            a = list(filter(None, re.split(r' |\n', f.readline())))
            pos[i][0] = float(a[0])
            pos[i][1] = float(a[1])
            pos[i][2] = float(a[2])
        #print(pos)
        return name, comment, _type, dimension, edge_weight_type,pos

def read_tour(dimension,path):
    with open(path,"r") as f:
        opt_tour = np.zeros(dimension)
        for i in range(5):
            f.readline()
        for j in range(dimension):
            opt_tour[j] = int(f.readline())
        return opt_tour


read_data("data/eil51.tsp")