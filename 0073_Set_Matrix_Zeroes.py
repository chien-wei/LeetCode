class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) space:
        # 1. check and store whether row 0 and col 0 has zero (time O(m + n))
        # 2. go over, if found matrix[i][j] == 0, set matrix[i][0], matrix[0][j] = 0, O(mn)
        # 3. go over rows and cols start from index 1, 
        #    if row or col head == 0, set entire row/col = 0, O(mn)
        # 4. if row 0 and col 0 has zero in step1., set those to 0, O(m + n)
        
        row0 = col0 = False
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                row0 = True
                break
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                col0 = True
                break
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][c] = 0
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(1, len(matrix[0])):
                    matrix[r][c] = 0
        if row0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if col0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        return