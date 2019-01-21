class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def isValid(board, i ,j):
            for col in range(3*3):
                if col != j and board[i][j] == board[i][col]:
                    return False
            for row in range(3*3):
                if row != i and board[i][j] == board[row][j]:
                    return False
            for row in range(i//3 * 3, (i//3+1) * 3):
                for col in range(j//3 * 3, (j//3+1) * 3):
                    if (row != i or col != j) and board[i][j] == board[row][col]:
                        return False
            return True
        
        def dfs(board, i, j):
            if i == len(board):
                return True
            if j >= len(board[0]):
                return dfs(board, i+1, 0)
            if board[i][j] == '.':
                for k in range(1, 3*3+1):  
                    board[i][j] = str(k)
                    if isValid(board, i, j):
                        if dfs(board, i, j+1):
                            return True
                    board[i][j] = '.'
            else:
                return dfs(board, i, j+1)
            return False
        
        dfs(board, 0, 0)
                            
                        