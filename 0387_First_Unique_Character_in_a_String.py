class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
            
        return -1