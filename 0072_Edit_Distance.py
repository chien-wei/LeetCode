# This solution based on https://web.stanford.edu/class/cs124/lec/med.pdf
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M, N = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M+1):
            dp[i][0] = i
        for j in range(N+1):
            dp[0][j] = j
        for i in range(1, M+1):
            for j in range(1, N+1):
                #print(i,j)
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+ (1 if word1[i-1] != word2[j-1] else 0))
        #print(dp)
        return dp[M][N]