class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        buffers = [''] * numRows
        i = 0
        d = 1
        for c in s:
            buffers[i] += c
            i += d
            if i == 0:
                d = 1
            elif i == numRows-1:
                d = -1
        return ''.join(buffers)