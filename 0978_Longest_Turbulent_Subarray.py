class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        inc, dec, mx = 1, 1, 1
        if len(A) < 2:
            return len(A)
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                dec = inc + 1
                inc = 1
            elif A[i] > A[i-1]:
                inc = dec + 1
                dec = 1
            else:
                inc = 1
                dec = 1
            mx = max(mx, inc, dec)
        return mx