class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        
        def dfs(grid, i, j):
            if not any(0 in row for row in grid) and grid[i][j] == 2:
                return 1
            if grid[i][j] == 2:
                return 0
            
            grid[i][j] = -1
            upath = 0
            for (k, l) in [(i+1, j+0), (i+0, j+1), (i-1, j+0), (i+0, j-1)]:
                if k >= 0 and k < M and l >= 0 and l < N and grid[k][l] != -1:
                    tmp = grid[k][l]
                    upath += dfs(grid, k, l)
                    grid[k][l] = tmp
            
            return upath
        
        i, j = 0, 0
        for k in range(M):
            for l in range(N):
                if grid[k][l] == 1:
                    i, j = k, l
                    break
        return dfs(grid, i, j)