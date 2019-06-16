from random import randint # randint(a, b) inclusive
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [] # [val]
        self.hash = {} # {val: index}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash:
            return False
        self.list.append(val) 
        self.hash[val] = len(self.list) - 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash:
            return False
        last = len(self.list) - 1
        lastVal = self.list[last]
        i = self.hash[val]
        self.list[i], self.list[last] = self.list[last], self.list[i]
        self.hash[lastVal] = i
        self.hash.pop(val)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[randint(0, len(self.list)-1)]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()