class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # starting from top-right
        # if target > matrix[r][c]: r + 1
        # if target < matrix[r][c]: c - 1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r, c = 0, len(matrix[0])-1
        while c >= 0 and r < len(matrix) and matrix[r][c] != target:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                break
        if c >= 0 and r < len(matrix) and matrix[r][c] == target:
            return True
        return False