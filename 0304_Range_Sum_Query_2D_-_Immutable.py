from copy import deepcopy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            return
        M, N = len(matrix), len(matrix[0])
        self.accMatrix = [[0 for _ in range(N+1)] for _ in range(M+1)] 
        # having first 0's row, col is easier
        for i in range(1, M+1):
            for j in range(1, N+1):
                self.accMatrix[i][j] = matrix[i-1][j-1] + self.accMatrix[i][j-1] + self.accMatrix[i-1][j] - self.accMatrix[i-1][j-1]
        print(self.accMatrix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        acc = self.accMatrix
        return acc[row2+1][col2+1] - acc[row2+1][col1] - acc[row1][col2+1] + acc[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)