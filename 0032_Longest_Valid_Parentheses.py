class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        ans = 0
        count = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')' and count > 0:
                dp[i] = 2 + dp[i-1] # handle (())
                if i - dp[i] > 0:
                    dp[i] += dp[i-dp[i]] # handle()()
                count -= 1
            ans = max(ans, dp[i])
        return ans