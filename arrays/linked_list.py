class Node:
    """
    An object for storing a single node of linked list. 
    Models  to attributes - data and link to the netx node in the list.
    """
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
         self.head = None