# http://www.cnblogs.com/grandyang/p/5677550.html

class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for hi in range(2, n+1):
            for lo in range(hi-1, -1, -1):
                global_min = float('inf')
                #print(lo, hi)
                for k in range(lo+1, hi):
                    local_max = k + max(dp[lo][k-1], dp[k+1][hi])
                    global_min = min(global_min, local_max)
                dp[lo][hi] = lo if lo+1 == hi else global_min
                #print(dp)
        return dp[1][n]