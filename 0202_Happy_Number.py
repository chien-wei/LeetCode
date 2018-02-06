class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n not in s:
            s.add(n)
            tmp = 0
            for c in list(str(n)):
                tmp += pow(int(c), 2)
            if tmp == 1:
                return True
            n = tmp
        return False