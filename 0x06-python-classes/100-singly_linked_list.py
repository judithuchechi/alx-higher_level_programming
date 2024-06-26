#!/usr/bin/python3
"""This module contains a class Square"""


class Node:
    ''' creates Square type '''
    def __init__(self, data, next_node=None):
        """
        Initialize a node with data and next_node.

        Parameters:
        - data: The data stored in the node.
        - next_node (Node): The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' creates a class of type singlylinked list '''
    def __init__(self):
        """Initialize a singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert new Node into the correct sorted position in the list
        Parameters:
        - value: The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            now = self.head
            while now.next_node is not None and now.next_node.data < value:
                now = now.next_node
            new_node.next_node = now.next_node
            now.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout."""
        result = ""
        now = self.head
        while now:
            result += str(now.data) + "\n"
            now = now.next_node
        return result.rstrip()
