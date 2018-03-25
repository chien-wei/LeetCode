class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        N = N*(N+1)//2
        for num in nums:
            N -= num
        return N