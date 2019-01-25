# first draft: TLE
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        to_pacific = [[False for _ in matrix[0]] for _ in matrix]
        to_atlantic = [[False for _ in matrix[0]] for _ in matrix]
        
        def recur1(matrix, i, j, visited):
            visited[i][j] = True
            if to_pacific[i][j] == True:
                return True
            
            if i == 0 or j == 0:
                to_pacific[i][j] = True
                return True

            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] <= matrix[i][j] and not visited[x][y]:
                    to_pacific[i][j] = to_pacific[i][j] or recur1(matrix, x, y, visited)
            return to_pacific[i][j]
                            
        def recur2(matrix, i, j, visited):
            visited[i][j] = True
            if to_atlantic[i][j] == True:
                return True
            
            if i == len(matrix)-1 or j == len(matrix[0])-1:
                to_atlantic[i][j] = True
                return True

            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] <= matrix[i][j] and not visited[x][y]:
                    to_atlantic[i][j] = to_atlantic[i][j] or recur2(matrix, x, y, visited)
            return to_atlantic[i][j]

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited1 = [[False for _ in matrix[0]] for _ in matrix]
                visited2 = [[False for _ in matrix[0]] for _ in matrix]
                recur1(matrix, i, j, visited1)
                recur2(matrix, i, j, visited2)
                #print(to_pacific)
                #print(to_atlantic)
                if to_pacific[i][j] and to_atlantic[i][j]:
                    res.append([i, j])
        return res

# Revised: accepted
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        to_pacific = [[False for _ in matrix[0]] for _ in matrix]
        to_atlantic = [[False for _ in matrix[0]] for _ in matrix]
        
        def dfs(matrix, i, j, visited):
            visited[i][j] = True

            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] >= matrix[i][j] and not visited[x][y]:
                    dfs(matrix, x, y, visited)
                    
        for i in range(len(matrix)):
            dfs(matrix, i, 0, to_pacific)
            dfs(matrix, i, len(matrix[0])-1, to_atlantic)
            
        for j in range(len(matrix[0])):
            dfs(matrix, 0, j, to_pacific)
            dfs(matrix, len(matrix)-1, j, to_atlantic)

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if to_pacific[i][j] and to_atlantic[i][j]:
                    res.append([i, j])
        return res