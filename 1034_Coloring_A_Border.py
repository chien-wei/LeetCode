class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        def dfs(grid, r, c, from_color, to_color, visited, new_grid):
            if visited[r][c]:
                return
            visited[r][c] = True
            neighbors = 0
            for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == from_color:
                    neighbors += 1
                    dfs(grid, x, y, from_color, to_color, visited, new_grid)
            if neighbors != 4:
                new_grid[r][c] = to_color
                   
                    
        new_grid = [[c for c in row] for row in grid]
        dfs(grid, r0, c0, grid[r0][c0], color, [[False for _ in grid[0]] for _ in grid], new_grid)
        
        return new_grid