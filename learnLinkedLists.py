# some imports
import sys
import time
from array import *


# Create the class node
class LisTNode:
    def __init__(self, data):
        """Constructor to initiate this object"""

        # store data
        self.data = data

        # store the reference (next item)
        self.next = None
        return

    def has_value(self, value):
        """Method to compare the value with the node data"""
        if self.data == value:
            return True
        else:
            return False


# Create a SingleLinkedList class
class SingleLinkedList:
    def __init__(self):
        """Constructor to initiate this object"""
        self.head = None
        self.tail = None
        return



    # Create a method that adds a node to the list
    def add_list_item(self, item):
        """ add an item at the end of the list """
        if not isinstance(item, LisTNode):
            item = LisTNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

# Instantiate some objects to the class node
node1 = LisTNode(15)
node2 = LisTNode(8.2)
node3 = LisTNode("Berlin")
