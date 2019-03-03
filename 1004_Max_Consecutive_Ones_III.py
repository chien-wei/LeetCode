class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # sliding window
        num_zero = 0
        mx = 0
        i, j = 0, 0
        while j < len(A):
            if A[j] == 0:
                num_zero += 1
            j += 1
            if num_zero > K:
                while i < len(A) and A[i] == 1:
                    i += 1
                i += 1
                num_zero -= 1
            mx = max(mx, j - i)
        return mx