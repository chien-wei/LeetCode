class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        i, j = 0, len(A)-1
        A.sort()
        res = -1
        while i < j:
            if A[i] + A[j] >= K:
                j -= 1
            else:
                res = max(res, A[i] + A[j])
                i += 1
            
        return res