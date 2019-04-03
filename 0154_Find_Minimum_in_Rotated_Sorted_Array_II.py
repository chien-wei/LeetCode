class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        
        if nums[0] == nums[-1]:
            return self.findMin(nums[:-1])
        
        mid_index = len(nums)//2
        mid = nums[mid_index]
        if mid < nums[0]:
            return self.findMin(nums[:mid_index + 1])
        elif nums[-1] < mid:
            return self.findMin(nums[mid_index:])
        else:
            return nums[0]