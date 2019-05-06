class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def string(index):
            return s[index-1]
        def pattern(index):
            return p[index-1]
        
        def patternHasStar(index):
            return True if index+1 < len(p)+1 and pattern(i+1) == "*" else False
        
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = True
        
        i, j = 1, 0
        while i < len(p)+1:
            if patternHasStar(i):
                i += 1
                while j < len(s)+1:
                    if (dp[i-2][j] or (dp[i][j-1] and ((j > 0 and string(j) == pattern(i-1)) or pattern(i-1) == "."))):
                        dp[i][j] = True
                    j += 1
            else:
                j = 1
                while j < len(s)+1:
                    if dp[i-1][j-1] and (string(j) == pattern(i) or pattern(i) == "."):
                        dp[i][j] = True
                    j += 1

            i += 1
            j = 0
            
        return dp[len(p)][len(s)] 