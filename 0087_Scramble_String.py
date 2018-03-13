"""
:type s1: str
:type s2: str
:rtype: bool
"""
# recursion
class Solution:
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            print(s1[:i], s1[i:], s1[-i:], s1[:-i])
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

# dp
# http://www.cnblogs.com/grandyang/p/4318500.html
class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        n = len(s1)
        dp = [[[False for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
        print(dp)
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        print(dp)
        for l in range(2, n+1):
            for i in range(n-l+1):
                for j in range(n-l+1):
                    for k in range(1, l):
                        print(l, i, j, k)
                        if (dp[i][j][k] and dp[i+k][j+k][l-k]) or (dp[i+k][j][l-k] and dp[i][j+l-k][k]):
                            dp[i][j][l] = True
                        print(dp)
        return dp[0][0][n]