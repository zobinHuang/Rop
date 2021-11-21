import numpy as np
from yaml import nodes
from src.node import node

# class:        topo
# description:  topology object
class topo:
    # function:     __init__()
    # description:  initialization function of a topo object
    # parameters:   topo_size: number of vertex in the graph
    # return value: none
    def __init__(self, topo_size:int):
        # size of topology (amount of nodes)
        self.size = topo_size

        # list of node objects
        self.node_list = list()
        
        # link situation among nodes (adjacency matrix)
        self.topo_matrix = np.mat(np.zeros((topo_size, topo_size)), int)

    # function:     add_node()
    # description:  add a node with specified node index
    # parameters:   node_index: index of current node
    # return value: none
    def add_node(self, node_index:int):
        n = node(node_index=node_index)
        self.node_list.append(n)

    # function:     get_node()
    # description:  return a node with specified index, return none if don't exist
    # parameters:   node_index: index of destinate node
    # return value: a node match to specified index, return none if don't exist
    def get_node(self, node_index:int):
        for node in self.node_list:
            if node.get_id() == node_index:
                return node
        return None

    # function:     add_link()
    # description:  add a link between two nodes with specified weight
    # parameters:   src_node: index of source node
    #               dest_node: index of source nodes
    #               weight: weight of current link (optional, default to be 1)
    # return value: none
    def add_link(self, src_node:int, dest_node:int, weight:int=1):
        self.topo_matrix[src_node, dest_node] = weight

    

    # function:     print_topo()
    # description:  print topology as adjacency matrix
    # parameters:   none
    # return value: none
    def print_topo(self):
        print(self.topo_matrix)
