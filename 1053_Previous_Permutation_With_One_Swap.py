# O(n^3) solution with very simple Python syntax: TLE
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        res = []
        B = A[:]
        i, j = 0, 1
        while i < len(A):
            j = i + 1
            while j < len(A):
                A[i], A[j] = A[j], A[i]
                if A > res and A < B:
                    res = A[:]
                A[i], A[j] = A[j], A[i]
                j += 1
            i += 1
        return res if res != [] else B

# Accepted logical solution
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        # find the first element we want to swap
        left_idx = -1
        mn = A[-1]
        for i in range(len(A) - 2, -1, -1):
            if A[i] < mn:
                mn = A[i]
            if A[i] > mn:
                left_idx = i
                break
        if left_idx == -1:
            return A
        
        # find largest element after left_idx that is smaller than A[left_idx] to swap
        # 
        right_idx = left_idx + 1
        mx = A[right_idx]
        for i in range(left_idx + 1, len(A)):
            if A[i] > mx and A[i] < A[left_idx]:
                mx = A[i]
                right_idx = i
        print(A[left_idx],A[right_idx])
        A[left_idx], A[right_idx] = A[right_idx], A[left_idx]
        return A
        