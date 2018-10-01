class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        B = sorted(list(set(A)))
        ans = B[-1] - B[0]
        for i in range(len(B)-1):
            mx = max(B[-1] - K, B[i] + K)
            mn = min(B[i+1] - K, B[0] + K)
            ans = min(ans, mx-mn)
        return ans