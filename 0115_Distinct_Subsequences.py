class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) == 0:
            return 1
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        for i in range(len(t)):
            for j in range(len(s)):
                if i == 0:
                    if s[j] == t[i]:
                        dp[i][j] = 1
                else:
                    if s[j] == t[i]:
                        dp[i][j] = sum(dp[i-1][0:j])
            if i == 0 and sum(dp[i]) < 1:
                return 0
        return sum(dp[len(t)-1])