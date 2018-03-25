class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        tb = []
        lr = []
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            lr.append(max(grid[i]))
        for j in range(N):
            m = 0
            for i in range(M):
                m = max(m, grid[i][j])
            tb.append(m)
        for i in range(M):
            for j in range(N):
                count += min(tb[j], lr[i]) - grid[i][j]
                
        return count