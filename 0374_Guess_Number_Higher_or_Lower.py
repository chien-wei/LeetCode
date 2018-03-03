# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        hi, lo = n, 1
        mi = (hi + lo) // 2
        res = guess(mi)
        while res != 0:
            if res == -1:
                hi, lo = mi-1, lo
                mi = (hi + lo) // 2
            elif res == 1:
                hi, lo = hi, mi+1
                mi = (hi + lo) // 2
            print(mi)
            res = guess(mi)
        
        return  mi