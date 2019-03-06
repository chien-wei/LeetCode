class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def num_win(board):
            win = {"X": 0, "O": 0}
            # rows
            if board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ':
                win[board[0][0]] += 1
            if board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ':
                win[board[1][0]] += 1
            if board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ':
                win[board[2][0]] += 1
            # cols
            if board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ':
                win[board[0][0]] += 1
            if board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ':
                win[board[0][1]] += 1
            if board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ':
                win[board[0][2]] += 1
            # diagonal
            if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
                win[board[0][0]] += 1
            if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
                win[board[0][2]] += 1
            
            return win
        
        def num_xo(board):
            # num_x - num_o
            num_x = 0
            num_o = 0
            for row in board:
                for col in row:
                    if col == 'X':
                        num_x += 1
                    elif col == 'O':
                        num_o += 1
            return num_x - num_o
        
        win = num_win(board)
        xo = num_xo(board)
        if win["X"] > 0 and win["O"] > 0:
            return False
        elif win["X"] > 0 and xo == 0:
            return False
        elif win["O"] > 0 and xo == 1:
            return False
        elif xo != 0 and xo != 1:
            return False
        return True