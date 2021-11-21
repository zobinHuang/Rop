# class:        node
# description:  node object
class node:
    # function:     __init__()
    # description:  initialization function of a node object
    # parameters:   node_index: index of current node
    # return value: none
    def __init__(self, node_index:int):
        self.id = node_index

    # function:     get_id()
    # description:  return the index of current node
    # parameters:   node
    # return value: the index of current node
    def get_id(self):
        return self.id