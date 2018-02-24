class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[1] if nums[1] and nums[1] > nums[0] else nums[0]
        
        n1, n2, n3 = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            print(n1, n2, n3)
            n1, n2, n3 = n2, n3, max(n1, n2) + nums[i]
        return max(n2,n3)