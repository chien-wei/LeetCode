class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # clockwise: reverse matrix row first than swap symmetry
        # anticlockwise: reverse each row first than swap symmetry
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r+1, len(matrix[r])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return