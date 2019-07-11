"""
Motivation:
key value search related cases. 
Directed access dict: key is integer map to value

Problems:
1. key may not exists.
2. memory abused

Solution:
1. prehashing: can always find a string of bits corresponding to a certain key
2. chaining: store the collision items in the same slot as a linked list

Chaining analysis:
expected length of chain for n keys, m slots = n/m aka load factor. As long as the m is O(n), we can get searching for constant time.

Hash functions:
1. division: h(k) = k mod m
3. multiplication method
2. universal hashing

New problems:
How to grow the table eg. how do we decide the load factor in order to get low insertion cost? (decide the value of m)  

# Table doubling 
Process:
- define a new dict with size m
- build new hash h
- insert each element with h  
How to decide the value of new m:
new_m = 2*m think of the cost of insertion.

# Amortization is the reason why choosing 2*m as the new size of the grown table.

"""
class RollingHash:
    def __init__(self, base, p):
        self.base = base
        self.p = p
        self.hash = 0
    
    def prehashing(self, value:str)->int:
        """
        Convert string to integer
        TODO
        """




def division_hash(value:int, m:int)->int:
    # m required to be random prime
    return value % m


##########################################
# table doubling 
##########################################
class MyDict:
    pass


##########################################
# string matching 
##########################################
class RollingHasher:
    # usage: hash(x.skip(c).append(c))
    def __init__(self, s):
        self.s = s
    def append(self, char):
        self.s = self.s + char
        return self
    def skip(self, char):
        """
        skip the first element which should be of value char, otherwise raise RuntimeError
        """
        if self.s[0]!=char:
            raise RuntimeError(f"skip the first element which should be of value {char}")
        self.s = self.s[1:]
        return self
    def __hash__(self):
        # TODO: use self defined hash function: division hash
        return hash(self.s)
    def __len__(self):
        return len(self.s)


class KarpRabin:
    def __init__(self, text, substring):
        self.text = text
        self.rolling_s = RollingHasher(substring)
        self.rolling_t = RollingHasher(text[:len(substring)])
    
    def match(self):
        if hash(self.rolling_s) == hash(self.rolling_t):
            # check char by char to avoid collision
            if self.rolling_s.s == self.rolling_t.s:
                return True
        new_rolling_t = self.rolling_t
        for c in self.text[len(new_rolling_t):]:
            if hash(self.rolling_s) == hash(new_rolling_t):
                if self.rolling_s.s == new_rolling_t.s:
                    return True
            new_rolling_t = new_rolling_t.skip(new_rolling_t.s[0]).append(c)
        return False
    

if __name__ == "__main__":
    print(KarpRabin("asdf  ferew324230vkxczoot4ijwgnvzir4", "zird").match())

    
