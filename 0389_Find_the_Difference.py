class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)