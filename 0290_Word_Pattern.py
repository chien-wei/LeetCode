class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        c1 = collections.Counter(str.split(' '))
        c2 = collections.Counter(pattern)
        s = str.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if c1[s[i]] != c2[pattern[i]]:
                return False
        return True