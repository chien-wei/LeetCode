class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        # sliding window
        num_zero = 0
        mx = 0
        i, j = 0, 0
        while j < len(A):
            if A[j] == 0:
                num_zero += 1
            j += 1
            if num_zero > 1:
                while i < len(A) and A[i] == 1:
                    i += 1
                i += 1
                num_zero -= 1
            mx = max(mx, j - i)
        return mx