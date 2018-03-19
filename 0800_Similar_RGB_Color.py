class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        r, g, b = color[1:3], color[3:5], color[5:7]
        res = '#'
        for c in [r, g, b]:
            if c[0] == c[1]:
                res += c[0] + c[1]
            elif c[0] > c[1]:
                if abs(int(c[0], 16) * 17 - int(c, 16)) > abs((int(c[0], 16)-1) * 17 - int(c, 16)):
                    tmp = hex(int(c[0], 16) - 1)[2:]
                    res += tmp + tmp
                else:
                    res += c[0] + c[0]
            elif c[0] < c[1]:
                if abs(int(c[0], 16) * 17 - int(c, 16)) > abs((int(c[0], 16)+1) * 17 - int(c, 16)):
                    tmp = hex(int(c[0], 16) + 1)[2:]
                    res += tmp + tmp
                else:
                    res += c[0] + c[0]
        return res