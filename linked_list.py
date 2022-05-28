from platform import *


class Node:
    """
    An object for storing a single node of linked list.\n
    Models  to attributes - data and link to the netx node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        return the no. of node in the list\n
        Takes o(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Add new node containing data at head of the list\n
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the frist node contatining data that matches the key\n
        return `Node` or `None` if data not foun\n
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position\n
        Insertion Takes O(1) time but finding the node at the insertion point takes O(n) time.\n

        Takes overll O(0) time
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removces  Node containing data that matches the key\n
        Returns the node or None if the key doesn't exist\n
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                 found = True
                 self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_noode = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return ' -> '.join(nodes)
