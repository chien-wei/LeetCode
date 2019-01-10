class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # First Naive Solution: get TLE
        '''
        if n == 0:
            return 1
        
        def num_bst(n1, n2):
            if n1 == n2:
                return 1
            elif n2 - n1 == 1:
                return 2
            else:
                ans = 0
                for i in range(n1, n2 + 1):
                    if i == n1:
                        ans += num_bst(n1+1, n2)
                    elif i == n2:
                        ans += num_bst(n1, n2-1)
                    else:
                        ans += num_bst(n1, i-1) * num_bst(i+1, n2)
                return ans
            
        return num_bst(1, n)
        '''

        # Turn First Solution to Top-down DP: accepted
        if n == 0:
            return 1
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        def num_bst(n1, n2, dp):
            if dp[n1][n2] != 0:
                return dp[n1][n2]
            if n1 == n2:
                dp[n1][n2] = 1
                return 1
            elif n2 - n1 == 1:
                dp[n1][n2] = 2
                return 2
            else:
                ans = 0
                for i in range(n1, n2 + 1):
                    if i == n1:
                        ans += num_bst(n1+1, n2, dp)
                    elif i == n2:
                        ans += num_bst(n1, n2-1, dp)
                    else:
                        ans += num_bst(n1, i-1, dp) * num_bst(i+1, n2, dp)
                dp[n1][n2] = ans
                return ans
            
        return num_bst(1, n, dp)

