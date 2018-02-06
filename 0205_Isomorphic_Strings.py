class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())


# Here is some good solutions:
# def isIsomorphic4(self, s, t): 
#     return [s.find(i) for i in s] == [t.find(j) for j in t]
    
# def isIsomorphic5(self, s, t):
#     return map(s.find, s) == map(t.find, t)