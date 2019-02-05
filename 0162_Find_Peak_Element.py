class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        
        if len(nums) == 1:
            return 0
        for i in range(0, len(nums)):
            if i == 0 and nums[0] > nums[1]:
                return 0
            elif i == len(nums)-1 and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return 0