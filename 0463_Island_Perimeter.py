class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if grid[i][j] == 1 and (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[i])):
                        res += 1
                    elif grid[i][j] == 1 and grid[r][c] == 0:
                        res += 1
        return res