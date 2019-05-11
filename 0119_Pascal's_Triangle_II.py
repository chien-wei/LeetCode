class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1, 1]
        for i in range(rowIndex-1):
            res = [1] + [res[i] + res[i+1] for i in range(len(res)-1)] + [1]
            
        return res