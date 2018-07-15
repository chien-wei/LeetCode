class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        import collections
        
        s = str(N)
        cn = collections.Counter([c for c in s])
        power2 = 1
        for i in range(30):
            cn2 = collections.Counter([c for c in str(power2)])
            if cn == cn2:
                return True
            power2 *= 2
            
        return False