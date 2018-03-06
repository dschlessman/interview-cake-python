"""superbalanced_btree

Implements a solution to `Superbalanced Binary Tree Checker`_ problem, problem 8, from Interview Cake.

A "superbalanced" binary tree is a tree where any two leaf nodes are at most one depth level apart.

Givens:
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = BinaryTreeNode(value)
            return self.right

.. _Temperature Tracker:
    #TODO
    https://www.interviewcake.com/question/python/temperature-tracker

"""
from typing import *

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

class BinaryTree(object):
    def __init__(self, head: BinaryTreeNode):
        self.tree = set()
        self.head = head

    def insert_node(self, node: BinaryTreeNode) -> int:
        self.tree.add(node)
        return 0

def is_superbalanced(tree: BinaryTree) -> bool:
    """Determines if a binary tree is 'superbalanced'

    A "superbalanced" binary tree is a tree where any two leaf nodes are at most
    one depth level apart.

    All nodes must be visisted to determine all possible branch depths, which
    can be done with breadth-first search or depth-first search Args: tree: a
    binary tree implemented as class BinaryTree in this module

    Raises: ValueError: if the tree violates the definition of a binary tree A
        binary tree's nodes must follow a rule where all left children are
        either all greater than the node value or all less than the node value.

    Returns: bool: if the tree is 'superbalanced'
    """
    head = tree.head
