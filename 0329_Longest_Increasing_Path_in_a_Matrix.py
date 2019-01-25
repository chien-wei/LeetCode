# First draft: TLE
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        # ans is list with only one integer, to become tail recursive
        def dfs(i, j, acc, ans):
            ans[0] = max(ans[0], acc)
            
            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    dfs(x, y, acc+1, ans)
            
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = [0]
                dfs(i, j, 1, ans)
                res = max(res, ans[0])
        return res

# Improve with DP: accepted
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in matrix[0]] for _ in matrix]
        
        def dfs(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            res = 1
            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1+dfs(x, y))
            dp[i][j] = res
            return res
            
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res
                