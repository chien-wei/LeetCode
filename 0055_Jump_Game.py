class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        jump = 0 + nums[0]
        i = 1
        while i <= jump and i < len(nums)-1:
            jump = max(jump, i + nums[i])
            i += 1
            
        if jump >= len(nums) - 1:
                return True
        return False