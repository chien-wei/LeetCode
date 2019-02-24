class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        M = len(board)
        N = len(board[0])
        rook_pos = []
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'R':
                    rook_pos = [i, j]
                    break
            if len(rook_pos) > 0:
                break
        count = 0
        for dir_x, dir_y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = rook_pos[0] + dir_x, rook_pos[1] + dir_y
            while x >= 0 and x < M and y >= 0 and y < N and board[x][y] == '.':
                x += dir_x
                y += dir_y
            if x >= 0 and x < M and y >= 0 and y < N and board[x][y] == 'p':
                count += 1
        return count