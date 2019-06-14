from collections import defaultdict
from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.k2vfre = {} # {key: (val, fre)}
        self.fre2kv = defaultdict(OrderedDict) # {fre: {key1: None, key2: None}, fre2:...}
        self.capacity = capacity
        self.minFre = 1
        

    def get(self, key: int) -> int:
        if key not in self.k2vfre:
            return -1
        val, fre = self.k2vfre.pop(key)
        self.fre2kv[fre].pop(key)
        if len(self.fre2kv[fre]) == 0 and fre == self.minFre:
            self.minFre += 1
        self.fre2kv[fre + 1][key] = None
        self.k2vfre[key] = (val, fre + 1)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.k2vfre: # update fre
            self.get(key)
            self.k2vfre[key] = (value, self.k2vfre[key][1])
            return
        
        if self.capacity <= len(self.k2vfre):
            delKey, _ = self.fre2kv[self.minFre].popitem(last=False) # pop first
            self.k2vfre.pop(delKey)
        self.k2vfre[key] = (value, 1)
        self.fre2kv[1][key] = None
        self.minFre = 1
                
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)