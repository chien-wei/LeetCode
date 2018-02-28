class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [(1,1)] * len(nums)
        _max = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i][0] < dp[j][0] + 1:
                    dp[i] = dp[j][0]+1, dp[j][1]
                    _max = max(_max, dp[i][0])
                elif nums[i] > nums[j] and dp[i][0] == dp[j][0] + 1:
                    dp[i] = dp[i][0], dp[i][1] + dp[j][1]
        ans = 0
        for tu in dp:
            if (tu[0] == _max):
                ans += tu[1]
        return ans