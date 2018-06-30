class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        ans = 0
        first = False
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                if grid[i][j] < 0 or grid[i][j] > 9:
                    continue
                elif grid[i][j-1] < 0 or grid[i][j-1] > 9:
                    continue
                elif grid[i][j-2] < 0 or grid[i][j-2] > 9:
                    continue
                elif grid[i-1][j] < 0 or grid[i-1][j] > 9:
                    continue
                elif grid[i-1][j-1] < 0 or grid[i-1][j-1] > 9:
                    continue
                elif grid[i-1][j-2] < 0 or grid[i-1][j-2] > 9:
                    continue
                elif grid[i-2][j] < 0 or grid[i-2][j] > 9:
                    continue
                elif grid[i-2][j-1] < 0 or grid[i-2][j-1] > 9:
                    continue
                elif grid[i-2][j-2] < 0 or grid[i-2][j-2] > 9:
                    continue
                elif grid[i-2][j-2] + grid[i-2][j-1] + grid[i-2][j] != 15:
                    continue
                elif grid[i-1][j-2] + grid[i-1][j-1] + grid[i-1][j] != 15:
                    continue
                elif grid[i][j-2] + grid[i][j-1] + grid[i][j] != 15:
                    continue
                elif grid[i-2][j-2] + grid[i-1][j-2] + grid[i][j-2] != 15:
                    continue
                elif grid[i-2][j-1] + grid[i-1][j-1] + grid[i][j-1] != 15:
                    continue
                elif grid[i-2][j] + grid[i-1][j] + grid[i][j] != 15:
                    continue
                elif grid[i-2][j-2] + grid[i-1][j-1] + grid[i][j] != 15:
                    continue
                elif grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2] != 15:
                    continue
                else:
                    ans += 1
                    
        return ans