class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    _min = float('inf')
                    for x, y in [(i-1, j), (i, j-1)]:
                        if x >= 0 and y >= 0:
                            _min = min(_min, dp[x][y])
                    dp[i][j] += grid[i][j] + _min
        return dp[M-1][N-1]