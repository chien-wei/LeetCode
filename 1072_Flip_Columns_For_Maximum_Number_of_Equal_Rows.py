class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        group = {}
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        for row in matrix:
            opp = [((i + 1) % 2) for i in row]
            group[tuple(row)] = group.get(tuple(row), 0) + 1
            group[tuple(opp)] = group.get(tuple(opp), 0) + 1
            
        return max(group.values())