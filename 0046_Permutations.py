class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.backtrack(ans, [], nums)
        return ans
    
    def backtrack(self, ans, tmp, nums):
        if not nums:
            ans.append(tmp)
        for i in range(len(nums)):
            self.backtrack(ans, tmp+[nums[i]], nums[:i]+nums[i+1:])