# Time: O(n^2), Space: O(n^2)
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        max_l = 1
        ans = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if max_l < 2:
                    max_l = 2
                    ans = s[i:i+2]
        

        for x in range(1, len(s)):
            for y in range(0, len(s)-x):
                i = y
                j = x + y
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > max_l:
                        max_l = j - i + 1
                        ans = s[i:j+1]
        return ans