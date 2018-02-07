class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        start, end = 0, 1
        res = 1
        for i in range(1, len(s)):
            while s[i] in s[start:end]:
                start += 1
            end += 1
            res = max(res, end-start)
        return res