class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        mx = 0
        idx2 = -1
        for i, c in enumerate('{:b}'.format(N)):
            if c == '1' and idx2 > -1:
                mx = max(mx, i - idx2)
                idx2 = i
            elif c == '1':
                idx2 = i
        return mx