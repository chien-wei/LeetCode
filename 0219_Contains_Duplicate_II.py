class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k >= len(nums):
            return True if len(nums) != len(set(nums)) else False
        h = {}
        for i in range(k+1):
            h[nums[i]] = h.get(nums[i], 0) + 1
            if h[nums[i]] > 1:
                return True
        for i in range(k+1, len(nums)):
            h[nums[i-k-1]] -= 1
            h[nums[i]] = h.get(nums[i], 0) + 1
            if h[nums[i]] > 1:
                return True
            
            
        return False