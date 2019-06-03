class LRUCache:
    # O(1) time complexity => get: need to have hashtable,
    # put: in order to keep order and manage capacity, we need double linked list. 
    # need to update hashtable too
    # if in hash, update head
    # if not in hash, fill until full, remove tail and update head if needed
    class DLLNode:
        def __init__(self, key, val):
            self.prev = None
            self.next = None
            self.key = key
            self.val = val
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = self.DLLNode(0, 0)
        self.tail = self.DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            res = self.dic[key].val
            node = self.dic[key]
            self._prepend(self._remove(node))
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self._prepend(self._remove(node))
        elif len(self.dic) < self.capacity:
            node = self.DLLNode(key, value)
            self._prepend(node)
            self.dic[key] = node
        else:
            self.dic.pop(self._pop().key)
            node = self.DLLNode(key, value)
            self._prepend(node)
            self.dic[key] = node
        
    def _prepend(self, node):
        nxt = self.head.next
        self.head.next, node.next = node, nxt
        node.prev, nxt.prev = self.head, node
        
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next, node.prev = None, None
        return node
    
    def _pop(self):
        node = self.tail.prev
        return self._remove(node)
            
    def printDLL(self):
        cur = self.head.next
        while cur:
            print(cur.key)
            cur = cur.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# use OrderedDict can be better
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)