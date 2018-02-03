class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        last = cur = 1
        for i in range(n-1):
            last, cur = cur, last+cur
        return cur