# bottom-up DP
# reference: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286753/C%2B%2B-with-picture
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for d in range(2, N):
            for i in range(0, N-d):
                j = i + d
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        return dp[0][N - 1]