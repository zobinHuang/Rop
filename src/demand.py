import numpy as np
from src.demand_pair import demand_pair

# class:        demand
# description:  demand object
class demand:
    # function:     __init__()
    # description:  initialization function of demand object               
    # parameters:   demand_amount: amount of demand pairs
    #               topo_size: size of topology
    # return value: none
    def __init__(self, demand_amount:int, topo_size:int):
        # amount of demand pairs
        self.amount = demand_amount
        
        # list of demand pairs
        self.pairs = list()

        # demand matrix among nodes (adjacency matrix)
        self.demand_matrix = np.mat(np.zeros((topo_size, topo_size)), int) 
    
    # function:     add_pair()
    # description:  add demand pair with specified source, destination and demand value
    # parameters:   src_node:       source node
    #               dest_node:      destination node
    #               demand:         demand value
    # return value: none
    def add_pair(self, src_node:int, dest_node:int, demand:int):
        # create demand pair obejct and append to list
        d = demand_pair(demand_index=len(self.pairs), src_node=src_node, dest_node=dest_node, demand=demand)
        self.pairs.append(d)

        # fullfill demand matrix
        self.demand_matrix[src_node, dest_node] = demand
    
    # function:     print_demand()
    # description:  print demand pairs as adjacency matrix
    # parameters:   none
    # return value: none
    def print_demand(self):
        print(self.demand_matrix)