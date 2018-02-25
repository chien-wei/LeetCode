class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {}
        for c in T:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        res = ""
        for c in S:
            if c in d:
                res += c
                while d[c] > 1:
                    res += c
                    d[c] -= 1
                d.pop(c)
        for k in d.keys():
            #print(k)
            res += k*d[k]
        return res