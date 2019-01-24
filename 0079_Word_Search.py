class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def findWord(board, word, i, j):
            if len(word) == 1 and board[i][j] == word[0]:
                return True
            if board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = '.'
            res = False
            for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] != '.':
                    res = res or findWord(board, word[1:], x, y)
            board[i][j] = tmp
            return res
            
        
        
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if findWord(board, word, row, col):
                    return True
        return False
                
        
                