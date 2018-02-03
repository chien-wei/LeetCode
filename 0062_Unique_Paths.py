class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [1] * n
        for i in range(m-1):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[n-1]