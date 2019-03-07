class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.count = 0
        ans = 0
        def dfs(i, j):
            if seen[i][j] == 1 or grid[i][j] == 0:
                return
            else:
                self.count += 1
                seen[i][j] = 1
                for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 1 and seen[x][y] == 0:
                            dfs(x, y)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
                ans = max(ans, self.count)
                self.count = 0
        return ans

# 2019/03/06 update:
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        
        def dfs(i, j):
            visited[i][j] = True
            res = 1
            for (x, y) in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if x >= 0 and x < M and y >= 0 and y < N and not visited[x][y] and grid[x][y] == 1:
                    res += dfs(x, y)
            return res
            
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, dfs(i, j))
        return res