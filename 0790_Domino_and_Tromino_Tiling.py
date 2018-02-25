class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 5
        if N == 4: return 11
        a,b,c,d = 1,2,5,11
        
        for i in range(N-4):
            a,b,c,d = b,c,d,d*2+b
        return d % 1000000007