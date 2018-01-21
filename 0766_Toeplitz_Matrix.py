class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        val = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] - matrix[i-1][j-1] != 0:
                    return False
        return True