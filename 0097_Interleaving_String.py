class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        X, Y, Z = len(s1), len(s2), len(s3)
        dp = [[None for _ in range(Y+1)] for _ in range(X+1)]
        def recur(s1, s2, s3, x, y, z):
            if dp[x][y] != None:
                return dp[x][y]
            
            res = False
            if z == Z and x == X and y == Y:
                dp[x][y] = True
                return True
            elif z < Z or (x < X and y < Y):
                if x < X and s3[z] == s1[x]:
                    res = res or recur(s1, s2, s3, x+1, y, z+1)
                if y < Y and s3[z] == s2[y]:
                    res = res or recur(s1, s2, s3, x, y+1, z+1)
                dp[x][y] = res
                return res
            else:
                dp[x][y] = False
                return False
                
        return recur(s1, s2, s3, 0, 0, 0)