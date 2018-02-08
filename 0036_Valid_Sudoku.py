class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in d:
                    return False
                elif board[i][j] != '.':
                    d[board[i][j]] = 1
            d = {}
            for j in range(len(board[0])):
                if board[j][i] != '.' and board[j][i] in d:
                    return False
                elif board[j][i] != '.':
                    d[board[j][i]] = 1
            d = {}
        
        for i in range(0, 7, 3):
            for k in range(0, 7, 3):
                for j in range(3):
                    for l in range(3):
                        if board[i+j][k+l] != '.' and board[i+j][k+l] in d:
                            return False
                        elif board[i+j][k+l] != '.':
                            d[board[i+j][k+l]] = 1
                d = {}
        return True

# TODO: other better solutions
# https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions