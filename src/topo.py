import numpy as np
from src.node import node

# class:        topo
# description:  topology object
class topo:
    # function:     __init__()
    # description:  initialization function of a topo object
    # parameters:   topo_size:      number of vertex in the graph
    #               is_bilateral:   whether bilateral link supported
    # return value: none
    def __init__(self, topo_size:int, is_bilateral:bool):
        # size of topology (amount of nodes)
        self.size = topo_size

        # whether bilateral link supported
        self.bilateral = is_bilateral

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

    # function:     check_legality()
    # description:  check legality of readin topology
    # parameters:   none
    # return value: None:   legal topology
    #               str:    illegal topology, error string returned
    def check_legality(self):
        # check whether the topology is undirectional indeed if it claimed it does not support bilateral link
        # (check whether the topo adjacency matrix is symmetric)
        if not self.bilateral:
            if not np.allclose(self.topo_matrix, self.topo_matrix.T, rtol=1e-05, atol=1e-08):
                return "illgeal topology since adjacency matrix isn't symmetric yet bilateral link is not supported"
        return None
