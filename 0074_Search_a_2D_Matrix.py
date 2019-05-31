class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(matrix: List[List[int]], target: int) -> List[int]:
            N = len(matrix)
            if N == 1:
                return matrix[0]
            
            midi = N // 2
            if matrix[midi][0] > target:
                return searchRow(matrix[:midi], target)
            else:
                return searchRow(matrix[midi:], target)
            
        def searchCol(ls: List[int], target: int) -> bool:
            print(ls)
            M = len(ls)
            if M == 1 and ls[0] == target:
                return True
            elif M == 1: 
                return False
            midi = M // 2
            if ls[midi] > target:
                return searchCol(ls[:midi], target)
            else:
                return searchCol(ls[midi:], target)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        return searchCol(searchRow(matrix, target), target)