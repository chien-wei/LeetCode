class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime2(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3,int(n**0.5)+1,2):   # only odd numbers
                if n%i==0:
                    return False    

            return True
        
        result = 0
        for n in range(L,R+1):
            if isPrime2(bin(n)[2:].count('1')):
                result += 1
            
        return result