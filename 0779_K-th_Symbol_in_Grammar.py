class Solution(object):
        
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        
        def helper(N, K, no):
            if K%2 == 0:
                no = not no
            #print(N, K, no)
            if N == 1 and K == 1:
                if no:
                    return 1
                return 0
            return helper(N-1, int(K / 2) + K%2, no)
        
        return helper(N, K, False)