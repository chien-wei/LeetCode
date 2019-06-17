class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] & 1 == 1:
                while i < j and A[j] & 1 != 0:
                    j -= 1
                A[i], A[j] = A[j], A[i]
                j -= 1
            i += 1
        return A