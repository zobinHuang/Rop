# class:        demand_pair
# description:  demand_pair object
class demand_pair:
    # function:     __init__()
    # description:  initialization function of a demand pair object
    # parameters:   demand_index:   index of current demand pair
    #               src_node:       index of source node within current demand pair
    #               dest_node:      index of destination node within current demand pair
    #               demand:         size of current demand pair
    # return value: none
    def __init__(self, demand_index:int, src_node:int, dest_node:int, demand:int):
        self.id = demand_index
        self.src = src_node
        self.dest = dest_node
        self.demand = demand
    
    # function:     get_id()
    # description:  return the index of current demand pair
    # parameters:   none
    # return value: the index of current demand pair
    def get_id(self):
        return self.id