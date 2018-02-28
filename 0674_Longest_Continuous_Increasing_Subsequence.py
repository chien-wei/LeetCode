class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        acc = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                acc += 1
                ans = max(ans, acc)
            else:
                acc = 1
        return ans