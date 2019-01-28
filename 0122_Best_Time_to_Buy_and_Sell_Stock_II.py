# first draft: TLE
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lo = float('inf')
        mx = 0
        for i in range(len(prices)):
            if prices[i] > lo:
                mx = max(mx, prices[i] - lo + self.maxProfit(prices[i+1:]))
            else:
                lo = prices[i]
        return mx


# dp optimized: Still get TLE on hard testcase
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [-1 for _ in range(len(prices))]
        def helper(i):
            if dp[i] >= 0:
                return dp[i]
            lo = prices[i]
            mx = 0
            for j in range(i+1, len(prices)):
                if prices[j] > lo:
                    mx = max(mx, prices[j] - lo + helper(j))
                else:
                    lo = prices[j]
            dp[i] = mx
            return mx
        res = 0
        for k in range(len(prices))[::-1]:
            res = max(res, helper(k))
        return res

# Actually, it can be solved just like this:
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total
        

