class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding windows
        # corner case: k <= 1 because multiply
        if k <= 1:
            return 0
        curVal, i, j, N = 1, 0, 0, len(nums)
        # if need to list all
        # res = []
        res = 0
        while j < N:
            curVal *= nums[j]
            
            while curVal >= k:
                curVal //= nums[i]
                i += 1
            
            #for a in range(0, j - i + 1):
            #   res.append(nums[j-a:j+1])
            res += j - i + 1
                
            j += 1
        return res