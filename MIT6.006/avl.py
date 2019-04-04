"""
This script contains note and code from MIT course about the avl tree

height of a node: longest path from it down to a leave = max(height(left), height(right))+1
depth of a node: root to the node
AVL tree definition: heights of left node and right node of every node to differ by at most 1 or -1
Adel'son-Vel'skii & Landis
"""
from abc import ABC
from bst import BSTNode

class AVLNode(BSTNode):
    def __init__(self, key, parent, height=1):
        """
        If it is a leave, left/right subtree's height are -1 
        Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
        """
        super(AVLNode, self).__init__(key, parent)
        self.height = height

    def update_height(self):
        left_height = self.get_left_subtree_height()
        right_height = self.get_right_subtree_height()
        self.height = max(left_height, right_height) + 1

    def get_left_subtree_height(self):
        if not self.lnode:
            return -1
        return self.lnode.height

    def get_right_subtree_height(self):
        if not self.rnode:
            return -1
        return self.rnode.height
    
    def left_rotate(self):
        """
        node's right tree is higher
        """
        right_subtree = self.rnode
        self.rnode = right_subtree.lnode
        right_subtree.lnode.parent = self
        if self.parent:
            if self is self.parent.lnode:
                self.parent.lnode = right_subtree
            if self is self.parent.rnode:
                self.parent.rnode = right_subtree
            right_subtree.parent = self.parent
        else:
            right_subtree.parent = None
        self.parent = right_subtree
        right_subtree.lnode = self
        self.update_height()
        self.lnode.update_height()
        self.rnode.update_height()

    def right_rotate(self):
        pass
    
    def rebalance(self):
        pass

    def validate(self):
        super(AVLNode, self).validate()
        left_height = self.get_left_subtree_height()
        right_height = self.get_right_subtree_height()
        if abs(left_height - right_height) > 1:
            raise RuntimeError("AVL property violation")


class AVL(ABC):
    """
            mid
            / \ 
           /   \ 
          /     \ 
      smaller   larger
    """
    def __init__(self, nodes):
        self.root = self.build(nodes)

    def build(self, nodes):
        root = nodes
        for node in nodes[1:]:
            pass
        return root

    def delete(self, node):
        pass
    
    def insert(self, node):
        """
        every time when you insert a node, check the balanced property
        """
        pass
    def min(self):
        pass
    
    def successor(self, node):
        """
        find next larger
        """
        pass
    
    def predecessor(self, node):
        """
        find next smaller
        """
        pass

    def is_balanced(self, node):
        """
        Define what is balanced
        """
        if node.leftTree.height - node.rightTree.height >= -1 \
            or node.leftTree.height - node.rightTree.height <= 1:
            return True 
        return False
    def balance(self, node):
        pass



if __name__ == "__main__":
    t = [1,12,23,78,9,5, 40, 50, 19]
    # TODO

