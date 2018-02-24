class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return
        nums.sort()
        res = float('-inf')
        
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums)-1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(target - res):
                    res = s
                if target - s == 0:
                    return s
                elif s -target > 0:
                    r -= 1
                else:
                    l += 1
        return res