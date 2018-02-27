class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        dp = [row[:] for row in matrix]
        M, N = len(matrix), len(matrix[0])
        ans = 0
        for i in range(M):
            for j in range(N):
                dp[i][j] = int(dp[i][j])
                if i > 0 and j > 0 and dp[i][j] > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    ans = max(ans, dp[i][j])
                elif dp[i][j] > 0:
                    ans = max(ans, 1)
        return ans*ans