# Dp solution same as 0123, get MLE
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        T = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                # not do any transaction on day j, or sell on day j when buy on day m
                for m in range(j):
                    T[i][j] = max(T[i][j], (prices[j] - prices[m]) + T[i-1][m])
                T[i][j] = max(T[i][j], T[i][j-1])
        return T[k][len(prices)-1]

# Accepted: state machine to DP
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        
        # if (times of transactions) > (max possible transactions), simple as 0122
        if k > N/2:
            ans = 0
            for i in range(1, N):
                ans += max(0, prices[i] - prices[i-1])
            return ans
        
        buy = [[0 for _ in range(k+1)] for _ in range(N+1)] # max profit at k transactions for day N buy
        sell = [[0 for _ in range(k+1)] for _ in range(N+1)] # max profit at k transactions for day N sell
        
        for j in range(1, k+1):
            buy[0][j] = float('-inf')
        for i in range(1, N+1):
            for j in range(1, k+1):
                buy[i][j] = max(buy[i-1][j], sell[i-1][j-1] - prices[i-1]) # a transaction are counted after a sell
                sell[i][j] = max(sell[i-1][j], buy[i-1][j] + prices[i-1])
        return sell[N][k]