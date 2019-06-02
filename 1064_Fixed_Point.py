class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, a in enumerate(A):
            if A[i] == i:
                return i
            elif A[i] > i:
                return -1
        return -1