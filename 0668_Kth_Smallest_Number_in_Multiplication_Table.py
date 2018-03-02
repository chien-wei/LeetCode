class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(x):
            return sum(min(n, int(x/i)) for i in range(1, m+1)) >= k
            
        low, high = 1, m*n
        while low < high:
            mi = int((low + high) / 2)
            if enough(mi):
                high = mi
            else:
                low = mi + 1
        return low