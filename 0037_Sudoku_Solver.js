/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    function isValid(board, i, j) {
        var col, row;
        for (col=0; col < 9; col++) {
            if (col !== j && board[i][j] === board[i][col]) return false;
        }
        for (row=0; row < 9; row++) {
            if (row !== i && board[i][j] === board[row][j]) return false;
        }
        for (row=Math.floor(i/3) * 3; row < Math.floor(i/3+1) * 3; row++) {
            for (col=Math.floor(j/3) * 3; col < Math.floor(j/3+1) * 3; col++) {
                if ((row !== i || col !== j) && board[i][j] === board[row][col]) return false;
            }
        }
        return true;
    }
    
    function dfs(board, i, j) {
        if (i === board.length) return true;
        if (j >= board[i].length) return dfs(board, i+1, 0);
        if (board[i][j] === '.') {
            for (var k=1; k < 9+1; k++) {
                board[i][j] = k.toString();
                if (isValid(board, i, j)) {
                    if (dfs(board, i, j+1)) {
                        return true;
                    }
                }
                board[i][j] = '.';
            }
        } else {
            return dfs(board, i, j+1);
        }
        return false;
    }
    dfs(board, 0, 0);
  };