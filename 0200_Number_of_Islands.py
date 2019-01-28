class Solution:
    def numIslands(self, matrix):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or matrix[0] == 0:
            return 0 

        def dfs(i, j, visited):
            visited[i][j] = True
            for (x, y) in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] == '1' and not visited[x][y]:
                    dfs(x, y, visited)

        visited = [[False for _ in matrix[0]] for _ in matrix]
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1' and not visited[i][j]:
                    dfs(i, j, visited)
                    res += 1
        return res
