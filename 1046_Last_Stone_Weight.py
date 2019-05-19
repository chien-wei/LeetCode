import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        que = queue.PriorityQueue()
        for stone in stones:
            que.put(-stone)
        
        while que.qsize() > 1:
            s1 = -que.get()
            s2 = -que.get()
            if s1 - s2 > 0:
                que.put(s2-s1)
            
        return -que.get() if que.qsize() == 1 else 0