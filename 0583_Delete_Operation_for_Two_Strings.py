class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        
        for i in range(0, M+1):
            for j in range(0, N+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1] else max(dp[i-1][j], dp[i][j-1])
        return M + N - 2 * dp[M][N]