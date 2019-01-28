def maxKilledEnemies(grid):
    M, N = len(grid), len(grid[0])
    rows = [[0 for _ in range(N)] for _ in range(M)]
    cols = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(M):
        srt = 0
        count = 0
        j = 0
        while j < N:
            if grid[i][j] == 'E':
                count += 1
            elif grid[i][j] == 'W':
                for k in range(srt, j):
                    rows[i][k] = count
                count = 0
                srt = j+1
            j += 1
        for k in range(srt, j):
            rows[i][k] = count

    for i in range(N):
        srt = 0
        count = 0
        j = 0
        while j < M:
            if grid[j][i] == 'E':
                count += 1
            elif grid[j][i] == 'W':
                for k in range(srt, j):
                    cols[j][i] = count
                count = 0
                srt = j
            j += 1
        for k in range(srt, j):
            cols[k][i] = count
    print(rows)
    print(cols)

    mx = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '0':
            	mx = max(mx, rows[i][j] + cols[i][j])

    return mx


print(maxKilledEnemies([['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]))