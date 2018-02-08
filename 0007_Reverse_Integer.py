class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = -int(str(x)[1:][::-1]) if str(x)[0] == '-' else int(str(x)[::-1])
        return res if res < 2**31-1 and res > -2**31 else 0