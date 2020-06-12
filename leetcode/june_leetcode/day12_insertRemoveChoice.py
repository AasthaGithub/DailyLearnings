#mine
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.l:
            return False
        self.l.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.l:
            self.l.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(tuple(self.l))

#80 ms Fastest
import random


class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.set = []
        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.set.append(val)
        self.index[val] = len(self.set) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        i = self.index[val]
        self.set[i] = self.set[-1]
        self.index[self.set[i]] = i
        del self.set[-1]
        del self.index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set)
