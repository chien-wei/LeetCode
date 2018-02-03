class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _min = float('inf')
        best = 0
        for price in prices:
            if price < _min:
                _min = price
            else:
                best = max(best, price - _min)
        return best