class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums.sort()
        index = 1
        ans = 1
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] >= index:
                index += 1
            if nums[i] > index:
                ans = index
                break
        if index == nums[-1]:
            ans = index + 1
        return ans