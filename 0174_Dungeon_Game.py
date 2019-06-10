# DFS: This solution gets TLE
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, i, j, acc, res):
            if i == len(matrix)-1 and j == len(matrix[0])-1:
                acc.append(matrix[i][j])
                res.append(acc)
                return res
            
            acc.append(matrix[i][j])
            for (x, y) in [(i+1, j), (i, j+1)]:
                if x < len(matrix) and y < len(matrix[0]):
                    dfs(matrix, x, y, acc[:], res)
            return res
        
        paths = dfs(dungeon, 0, 0, [], [])
        lows = []
        for path in paths:
            acc = 0
            lowest = 0
            for p in path:
                acc += p
                lowest = min(lowest, acc)
            lows.append(lowest)
        
        return -max(lows) + 1

# dp: Accepted
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # fill dp table from princess
        # dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        # we can intialize dp with MAX_INT because we are looking for minimum health
        # for the right and down cell of princess, we set them 1 because that is minimum health
        # when the knight arrived
        M, N = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(N+1)] for _ in range(M+1)]
        dp[M][N-1] = 1
        dp[M-1][N] = 1
        
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
                
        return dp[0][0]
                