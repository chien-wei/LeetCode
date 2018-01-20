# TODO: how to do the same thing in one time n^2 loop and use only one 2D list

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        matrix = [[1 for i in range(N)] for j in range(N)]
        for t in mines:
            matrix[t[0]][t[1]] = 0
        up = [i[:] for i in matrix]
        down = [i[:] for i in matrix]
        left = [i[:] for i in matrix]
        right = [i[:] for i in matrix]
        
        for i in range(N):
            for j in range(N):
                if i > 0 and up[i][j] > 0 and up[i-1][j] > 0:
                    up[i][j] = up[i-1][j]+1
                if j > 0 and left[i][j] > 0 and left[i][j-1] > 0:
                    left[i][j] = left[i][j-1]+1
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if j < N-1 and right[i][j] > 0 and right[i][j+1] > 0:
                    right[i][j] = right[i][j+1]+1
                if i < N-1 and down[i][j] > 0 and down[i+1][j] > 0:
                    down[i][j] = down[i+1][j]+1
        
        result = 0
        for i in range(N):
            for j in range(N):
                min_plus = min(up[i][j], down[i][j], left[i][j], right[i][j])
                result = max(min_plus, result)
        return result