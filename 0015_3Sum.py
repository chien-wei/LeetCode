class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.nSum(nums, 0, 3, [], res)
        return res
    
    def nSum(self, nums, target, n, result, results):
        #print(nums, target, n, result, results)
        if len(nums) < n or n < 2:
            return
        if n == 2:
            l, r = 0, len(nums)-1
            while r > l:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                        
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-n+1):
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target - nums[i], n-1, result+[nums[i]], results)
        return