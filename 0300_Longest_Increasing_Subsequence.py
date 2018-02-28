class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = 1
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    ans = max(ans, dp[i])
        return ans