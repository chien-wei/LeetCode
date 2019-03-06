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

# 2019/03/06 update:
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        exist = {}
        result = 0
        while j < len(s):
            if s[j] not in exist:
                exist[s[j]] = 1
            else:
                while i < j and s[i] != s[j]:
                    exist.pop(s[i])
                    i += 1
                i += 1
            j += 1
            result = max(result, j-i)
            
        return result