from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 8-direction bfs
        if len(grid) == 0 or grid[0][0] == 1:
            return -1
        M, N = len(grid), len(grid[0])
        deq = deque()
        deq.append((0,0))
        step = 0
        while len(deq) > 0:
            step += 1
            nxt = deque()
            while len(deq) > 0:
                i, j = deq.popleft()
                for x, y in [(i+1, j+1), (i+1, j), (i, j+1), (i+1, j-1), (i, j-1), (i-1, j+1), (i-1, j), (i-1, j-1)]:
                    if x >= 0 and x < M and y >= 0 and y < N and (x, y) and grid[x][y] == 0:
                        nxt.append((x, y))
                        grid[x][y] = 1 # set to 1 first to prevent duplicate
                        if x == M-1 and y == N-1:
                            return step + 1
            deq = nxt
        return -1