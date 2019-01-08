class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        dp = [row[:] for row in matrix]
        M, N = len(matrix), len(matrix[0])
        ans = 0
        for i in range(M):
            for j in range(N):
                dp[i][j] = int(dp[i][j])
                if i > 0 and j > 0 and dp[i][j] > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    ans = max(ans, dp[i][j])
                elif dp[i][j] > 0:
                    ans = max(ans, 1)
        return ans*ans

# 2019/01/08
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Brute Force 
        '''
        def square_submatrix(matrix, i, j):
            if i == len(matrix) or j == len(matrix[0]) or matrix[i][j] == '0':
                return 0
            ans = 1 + min(square_submatrix(matrix, i+1, j),
                          square_submatrix(matrix, i, j+1),
                          square_submatrix(matrix, i+1, j+1))
            return ans
        
        M, N = len(matrix), len(matrix[0])
        mx = 0
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j]:
                    mx = max(mx, square_submatrix(matrix, i, j))
        
        return mx*mx
        '''
        
        # Top-down DP
        '''
        def square_submatrix(matrix, i, j, dp):
            if i == len(matrix) or j == len(matrix[0]) or matrix[i][j] == '0':
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            dp[i][j] = 1 + min(square_submatrix(matrix, i+1, j, dp),
                          square_submatrix(matrix, i, j+1, dp),
                          square_submatrix(matrix, i+1, j+1, dp))
            
            return dp[i][j]
        
        if len(matrix) < 1:
            return 0
        M, N = len(matrix), len(matrix[0])
        mx = 0
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j]:
                    mx = max(mx, square_submatrix(matrix, i, j, dp))
        
        return mx*mx
        '''
        # Bottom-up DP
        if len(matrix) < 1:
            return 0
        M, N = len(matrix), len(matrix[0])
        mx = 0
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                mx = max(mx, dp[i][j])
        
        return mx*mx