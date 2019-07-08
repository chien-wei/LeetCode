class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        if K == 1:
            return True
        
        # maximum number of an element
        cur, acc, mx = 0, 0, 0
        for num in nums:
            if num != cur:
                mx = max(mx, acc)
                cur = num
                acc = 0
            acc += 1
        mx = max(mx, acc)
        if len(nums) < K * mx:
            return False
        return True