class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = A[0] + K
        l = A[0] - K
        for i in range(1, len(A)):
            s = min(A[i] + K, s)
            l = max(A[i] - K, l)
        if s >= l:
            return 0
        return l-s

#Or just return max(0, max(A) - min(A) - 2 * K)