class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        N = len(obstacleGrid)
        if N == 0: return 0
        M = len(obstacleGrid[0])
        if M == 0: return 1
        if obstacleGrid[0][0] == 1: return 0
        dp = [[0 for _ in range(M)] for _ in range(N)] 
        dp[0][0] = 1
        for i in range(N):
            for j in range(M):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    for x, y in [(i-1, j), (i, j-1)]:
                        if x >= 0  and y >= 0:
                            dp[i][j] += dp[x][y]
        return dp[N-1][M-1]