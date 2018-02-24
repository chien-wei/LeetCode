class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        
        # we use 2 table, one starting from index 0 to n-1, one starting from index 1 to n
        # at the end, we compare the last value for both table
        n1, n2, n3 = nums[0], nums[1], nums[2]+nums[0]
        m1, m2, m3 = nums[1], nums[2], nums[3]+nums[1]
        for i in range(3, len(nums)-1):
            n1, n2, n3 = n2, n3, max(n1, n2) + nums[i]
            m1, m2, m3 = m2, m3, max(m1, m2) + nums[i+1]
        return max(n2, n3, m2, m3)