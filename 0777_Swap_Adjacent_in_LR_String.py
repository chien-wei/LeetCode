class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
        if len(s) != len(e):
            return False
        for z in zip(s, e):
            if z[0][0] != z[1][0]:
                return False
            if z[0][0] == 'L' and z[0][1] < z[1][1]:
                return False
            elif z[0][0] == 'R' and z[0][1] > z[1][1]:
                return False
        return True

# or use 
# return len(s) == len(e) and all(c1 == c2 and (i1 >= i2 and c1 == 'L' or i1 <= i2 and c1 == 'R') for (c1, i1), (c2, i2) in zip(s,e))