class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            cand = []
            for j in coins:
                if i - j < 0:
                    cand.append(float('inf'))
                else:
                    cand.append(dp[i-j])
            dp[i] = min(cand) + 1
        return dp[amount] if dp[amount] != float('inf') else -1