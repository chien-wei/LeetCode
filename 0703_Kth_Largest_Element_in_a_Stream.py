# Use PriorityQueue
import queue
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.mx = queue.PriorityQueue()
        self.mn = queue.PriorityQueue()
        for num in nums:
            self.mx.put(-num)
        for i in range(k-1):
            tmp = -self.mx.get()
            self.mn.put(tmp)
            
    def top(self, heap):
        tmp = heap.get()
        heap.put(tmp)
        return tmp

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if not self.mx.empty() and val <= -self.top(self.mx):
            self.mx.put(-val)
        else:
            self.mn.put(val)
            self.mx.put(-self.mn.get())
        return -self.top(self.mx)
            

# Use heapq

from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.mx = []
        self.mn = []
        for num in nums:
            heappush(self.mx, -num)
        for i in range(k-1):
            heappush(self.mn, -heappop(self.mx))
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.mx) > 0 and val <= -self.mx[0]:
            heappush(self.mx, -val)
        else:
            heappush(self.mn, val)
            heappush(self.mx, -heappop(self.mn))
        return -self.mx[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)