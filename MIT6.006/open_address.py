"""
Instead of chaing, we use constantly probing new empty slot for a new key


Linear probing: h(k) = (ord(k) + i) mod m
Problem: 
    clustering
Solution:
    Double hashing: h(k) = (ord1(k) + i*ord2(k)) mod m (where m is odd, ord2(k) 
    is pow(2,r) so that they are relatively prime 
"""


class SlotStatus:
    empty = 1
    deleted = 2
    occupied = 3


class OpenAddressHasher:
    """
    Illustrate how to resolve collision using open address method
    """
    def __init__(self, size):
        self.table = dict.fromkeys(range(size))
        self.elements = 0
        self.load_factor = 0
    
    def update_load_factor(self, insert=True):
        if insert:
            assert self.load_factor != 1
            self.load_factor = (self.elements+1)/len(self.table)
        else:
            assert self.load_factor != 0
            self.load_factor = (self.elements-1)/len(self.table)

    def insert(self, key):
        h = self.division_hashing(key)
        if self.table.get(h) is None or self.table.get(h) == "deleted":
            self.table[h] = key
            self.update_load_factor(True)
            return True
        shift = self.linear_probing(key, h)
        if shift != -1:
            self.update_load_factor(True)
            self.table[shift] = key
            return True
        else:
            return False
    
    def linear_probing(self, key, i):
        """
        @param i: the level of probing 
        Probe if the current position is occupied or not, if it is, call it 
        recursively until it return None or out of the size
        """
        h = self.division_hashing(key)
        if self.table.get(h) is None:
            return i
        # meaning already traversed all the keys in the table
        if h == i: 
            return -1
        return self.linear_probing(key, i+1)

    def search(self, key):
        h = self.division_hashing(key)
        if self.table.get(h) is None or self.table.get(h) == "deleted":
            return -1
        if self.table[h] == key:
            return h
        else:
            return self.linear_probing(key, h)
    
    def delete(self, key):
        h = self.division_hashing(key)
        # note that delete is just going to mark the slot as deleted
        if self.table.get(h) is None or self.table.get(h) == "deleted":
            return False
        else:
            self.table[h] = "deleted"
            self.update_load_factor(False)
            return True

    def division_hashing(self, key):
        return hash(key) % len(self.table)

    def double_hashing_probing(self, key, i):
        # TODO: this is to solve the linear probing's clustering issue 
        h1 = hash(key)
        # simple sceanario: make sure the length of the table is 
        h2 = h1/10 + 1 if h1/10 % 2 == 0 else h1 / 10  # make the second hash value odd
        return (h1 + i*h2) % len(self.table)
