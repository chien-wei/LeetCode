# First draft: O(n^n), TLE
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def helper(prices, i, left):
            if left == 0 or i >= len(prices)-1:
                return 0
            mx = 0
            lo = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] > lo:
                    mx = max(mx, prices[j] - lo + helper(prices, j+1, left-1), helper(prices, j+1, left))
                else:
                    lo = prices[j]
            return mx

        return helper(prices, 0, 2)


# Dp solution: O(kn^2) Still get TLE
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        T = [[0 for _ in range(len(prices))] for _ in range(3)]
        for i in range(1, 3):
            for j in range(1, len(prices)):
                # not do any transaction on day j, or sell on day j when buy on day m
                for m in range(j):
                    T[i][j] = max(T[i][j], (prices[j] - prices[m]) + T[i-1][m])
                T[i][j] = max(T[i][j], T[i][j-1])
        return T[2][len(prices)-1]


# Dp solution: O(n) Accepted
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        b1 = float('-inf')
        s1 = 0
        b2 = float('-inf')
        s2 = 0
        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1 + p)
            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)
        return s2