class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hs = {}
        ht = {}
        for i in range(len(s)):
            hs[s[i]] = hs[s[i]] + 1 if s[i] in hs else 1
            ht[t[i]] = ht[t[i]] + 1 if t[i] in ht else 1
            print(hs, ht)
            if hs[s[i]] != ht[t[i]]:
                return False
        return True