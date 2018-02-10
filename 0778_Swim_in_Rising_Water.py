from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = []
        seen = {(0, 0)}
        _max = grid[0][0]
        heappush(h, (grid[0][0], 0, 0))
        while h:
            cur, x, y= heappop(h)
            _max = max(_max, cur)
            if x == y == len(grid)-1: return _max
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in seen:
                    heappush(h, (grid[nx][ny], nx, ny))
                    seen.add((nx, ny))

# TODO: There are also Dijkstra, BFS, DFS solutions, try them