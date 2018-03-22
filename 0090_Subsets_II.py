class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.backtrack(ans, [], nums, 0)
        return ans
        
        
    def backtrack(self, ans, tmp, nums, start):
        #print(nums, tmp, start, ans)
        ans.append(tmp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.backtrack(ans, tmp, nums, i+1)
            tmp.pop()