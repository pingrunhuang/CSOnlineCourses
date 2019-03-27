"""
This note is about the knowledge and note of Binary search tree and BST Sort
Runway Reservation System
* Airport with single (very busy) runway (Boston 6 -> 1)
* "Reservations" for future landings
* When plane lands, it is removed from set of pending events
* Reserve req specify "requested landing time" t
* Add t to the set if no other landings are scheduled within k minutes either way.
    Assume that k can vary.
    – else error, don’t schedule

Essentially the problem above require the following invariant:
1. Fast insertion
2. Fast lookup

how to get number of time before T? subtrees concept 

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec05.pdf


Best practice for cs thinking: decomposition ->  
"""

class BSTNode:
    def __init__(self, key, parent=None):
        """
        Keep parent in order for rotate: double linked list
        aka subtree of BST
        """
        self.key = key
        self.lnode = None
        self.rnode = None
        self.parent = parent
    def __le__(self, other):
        return self.key <= other.key
    def __lt__(self, other):
        return self.key > other.key
    def __eq__(self, other):
        return self.key == other.key
    def __gt__(self, other):
        return self.key > other.key
    def __ge__(self, other):
        return self.key >= other.key
    def update_child(self, node, direction='left'):
        if direction not in ('left', 'right'):
            return None
        if direction == 'left':
            self.lnode = node 
        if direction == 'right':
            self.rnode = node
        if node is not None:
            node.parent = self
        return node
    def insert(self, node):
        """
        traversal insert and remember to update parent and child relationship: O(lgN)
        """
        if node < self:
            if self.lnode:
                self.lnode.insert(node)
                return True
            else:
                node = self.update_child(node, 'left')
                return True
        elif node > self:
            if self.rnode:
                self.rnode.insert(node)
                return True
            else:
                self.update_child(node, 'right')
                self.rnode = node
            return True
        else:
            return False
    def delete(self):
        """
        delete this node from a bst: tricky to implement

                        20
                        /\ 
                       10 23
                       /\  /\ 
                      8 14 22 30
        delete 10 -> find the next node just larger then 10 
        return the deleted node
        """
        if self.rnode is None or self.lnode is None:
            if self.parent and self is self.parent.lnode:
                self.parent.update_child(self.lnode, direction='left') if self.lnode \
                    else self.parent.update_child(self.rnode, direction='left')
            elif self.parent and  self is self.parent.rnode:
                self.parent.update_child(self.lnode, direction='right') if self.lnode \
                    else self.parent.update_child(self.rnode, direction='right')
            else:
                # self.parent is none, root
                if self.rnode is not None:
                    self.rnode.parent = None  
                else:
                     self.lnode.parent = None
            return self
        else:
            subsitute = self.next_larger()
            # swap from up to bottom
            self.key , subsitute.key = subsitute.key, self.key
            return subsitute.delete()

    def next_larger(self):
        """
        delete related

        return an element just larger then the current node. None if the current node is root
        """
        if self.rnode:
            return self.rnode.find_min()
        ptr = self
        # TODO: Hard to imagine
        while ptr.parent and ptr is ptr.parent.rnode:
            # the only way to not return None is to break the ptr is ptr.parent.rnode condition
            ptr = ptr.parent
        return ptr.parent

    def find_min(self):
        """
        delete related
        """
        ptr = self
        while ptr.lnode is not None:
            ptr = ptr.lnode
        return ptr
    def find(self, node):
        """
        O(lgN)
        """
        if node == self:
            return self
        else:
            if node < self:
                if self.lnode:
                    return self.lnode.find(node)
                else:
                    return None
            if node > self:
                if self.rnode:
                    return self.rnode.find(node)
                else:
                    return None
        return None
    def validate(self):
        """
        raise exception when violating the bst properties
        """
        if self.lnode is not None:
            if self.lnode.key > self.key:
                raise RuntimeError("BST violated by a left node key")
            if self.lnode.parent is not self:
                raise RuntimeError("BST violated by a left node parent pointer")
            self.lnode.validate()
        if self.rnode is not None:
            if self.rnode.key < self.key:
                raise RuntimeError("BST violated by a right node key")
            if self.rnode.parent is not self:
                raise RuntimeError("BST violated by a right node parent pointer")
            self.rnode.validate()
import sys
class BST:
    """
    support insert, delete, bst properties validation, find, next_larger
    """
    def __init__(self, klass=BSTNode):
        self.root = None
        self.klass = klass
    def insert(self, k):
        node = self.klass(k, None)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
    def find(self, k):
        if self.root is None:
            raise Exception("Empty tree")
        node = BSTNode(k)
        return self.root.find(node)
    def delete(self, k):
        if self.root is None:
            raise Exception("Empty tree")
        node = self.find(BSTNode(k))
        if node is None:
            return None
        if node == self.root:
            # append a pseudoroot to the current root
            pseudoroot = self.klass(-sys.maxsize, None)
            self.root.parent = pseudoroot
            pseudoroot.rnode = self.root
            deleted = self.root.delete()
            self.root = pseudoroot.rnode
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()
    def bst_property_validation(self):
        if self.root is not None:
            if self.root.parent is not None:
                raise Exception("Root parent should be empty")
            self.root.validate()

class RunWayReservationSystem(BST):
    """
    essentially is the implementation of min bst
    """

    def __init__(self, times):
        pass
    
    def left_rotate(self, node):
        pass


if __name__ == "__main__":
    t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 