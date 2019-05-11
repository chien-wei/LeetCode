class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return[[1]]
        res = [[1], [1, 1]]
        for i in range(numRows-2):
            res.append([1] + [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)] + [1])
            
        return res