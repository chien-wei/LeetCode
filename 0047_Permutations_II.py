class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        self.backtrack(ans, [], nums, used)
        return ans
    
    def backtrack(self, ans, tmp, nums, used):
        #print(tmp, nums, ans)
        if len(tmp) == len(nums):
            ans.append(tmp)
        else:
            for i in range(len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                self.backtrack(ans, tmp + [nums[i]], nums, used)
                used[i] = False