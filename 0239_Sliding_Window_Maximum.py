from collections import deque
# like list, but list takes O(n) for pop(0), insert(v, 0)
# deque has popleft, appendleft which takes O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        deq = deque()
        res = []
        
        for i in range(k):
            while len(deq) > 0 and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        
        for i in range(k, len(nums)):
            res.append(nums[deq[0]])
            if i - k >= deq[0]:
                deq.popleft()
            while len(deq) > 0 and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        res.append(nums[deq[0]])
            
        return res