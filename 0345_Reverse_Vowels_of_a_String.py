class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while j > i:
            while j >= 0 and s[j] not in vowels:
                j -= 1
            while i < len(s) and s[i] not in vowels:
                i += 1
            if j > i:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                j -= 1
                i += 1
        return s