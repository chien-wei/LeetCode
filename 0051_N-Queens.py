class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(n, row, d45, d90, d135, acc, res):
            if row == n:
                res.append(acc)
            for col in range(n):
                if col not in d90 and row+col not in d45 and row-col not in d135:
                    d90[col] = True
                    d45[row+col] = True
                    d135[row-col] = True
                    acc.append("." * (col-0) + "Q" + "." * (n-col-1))
                    backtrack(n, row+1, d45, d90, d135, acc[:], res)
                    acc.pop()
                    d90.pop(col)
                    d45.pop(row+col)
                    d135.pop(row-col)
        res = []
        backtrack(n, 0, {}, {}, {}, [], res)
        return res