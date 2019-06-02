# O(n^3): accepted, beat 100% runtime & memory
# For each col, compute the accumulated value from row1 ~ row2, put in list 'acc'
# There are O(n^2) way for (row1, row2)
# For list acc, now the problem simplify to finding target with col2 - col1
# There are O(n^2) way for (col1, col2), but we can use hashtable to optimize

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        res = 0
        for i in range(len(matrix)):
            acc = [0 for _ in range(len(matrix[0]))]
            
            for t in range(i, len(matrix)):
                for j in range(len(acc)):
                    acc[j] += matrix[t][j]
                
                preSum = 0
                preSet = {preSum: 1}
                
                for j in range(len(acc)):
                    preSum += acc[j]
                    tmp = preSum - target
                    if tmp in preSet:
                        res += preSet[tmp]
                    preSet[preSum] = preSet.get(preSum, 0) +  1
        return res