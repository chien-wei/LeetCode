def shortestDist(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    M, N = len(grid), len(grid[0])
    sum_grid = [[0 if grid[i][j] == 0 else float('inf') for j in range(N)] for i in range(M)]

    num_build = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                # bfs
                level_grid = [[0 for j in range(N)] for i in range(M)]
                que = [(i, j)]
                while len(que) > 0:
                    (m, n) = que.pop(0)
                    for (x, y) in [(m+1, n), (m-1, n), (m, n+1), (m, n-1)]:
                        if x >= 0 and x < M and y >= 0 and y < N and grid[x][y] == 0 and level_grid[x][y] == 0:
                            que.append((x, y))
                            level_grid[x][y] = level_grid[m][n] + 1
                print(level_grid)
                for m in range(M):
                    for n in range(N):
                        if level_grid[m][n] == 0:
                            sum_grid[m][n] += float('inf')
                        else:
                            sum_grid[m][n] += level_grid[m][n]
                print(sum_grid)
            

    res = float('inf')
    for i in range(M):
        for j in range(N):
            res = min(res, sum_grid[i][j])
    if res == float('inf'):
        return -1
    return res


print(shortestDist([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print(shortestDist([[1,2,0,0,1],[2,0,0,0,1]]))
print(shortestDist([[0,1,2,0,0],[0,2,0,0,1]]))