class Solution {
    private Boolean isValid(char[][] board, int i, int j) {
        for (int col=0; col < 9; col++) {
            if (col != j && board[i][j] == board[i][col]) return false;
        }
        for (int row=0; row < 9; row++) {
            if (row != i && board[i][j] == board[row][j]) return false;
        }
        for (int row=i/3 * 3; row < (i/3 + 1) * 3; row++) {
            for (int col=j/3 * 3; col < (j/3 + 1) * 3; col++) {
                if ((row != i || col != j) && board[i][j] == board[row][col]) return false;
            }
        }
        return true;
    }
    
    private Boolean DFS(char[][] board, int i, int j) {
        if (i == board.length) return true;
        if (j == board[i].length) return DFS(board, i+1, 0);
        if (board[i][j] == '.') {
            for (int k=1; k < 10; k++) {
                board[i][j] = (char)(k + '0');
                if (isValid(board, i, j) && DFS(board, i, j+1)) {
                    return true;
                }
                board[i][j] = '.';
            }
        } else {
            return DFS(board, i, j+1);
        }
        return false;
    }
    
    public void solveSudoku(char[][] board) {
        DFS(board, 0, 0);
    }
}