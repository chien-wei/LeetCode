# dfs
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

# union-find
class Solution:
    def numIslands(self, matrix):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        M, N = len(matrix), len(matrix[0])
        parent = [i for i in range(M*N)]
        self.count = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    self.count += 1
        
        def find(id1):
            if parent[id1] == id1:
                return id1
            return find(parent[id1])
        
        def union(id1, id2):
            f1 = find(id1)
            f2 = find(id2)
            if f1 != f2:
                parent[f1] = f2
                self.count -= 1
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if x >= 0 and x < M and y >= 0 and y < N and matrix[x][y] == '1':
                            id1 = i*N + j
                            id2 = x*N + y
                            union(id1, id2)
        return self.count

# union-find optimized by rank and path compression
