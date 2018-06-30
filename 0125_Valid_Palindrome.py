class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        valid = True
        while j > i:
            while not s[i].isalnum() and j > i:
                i += 1
            c1 = s[i].lower()
            while not s[j].isalnum() and j > i:
                j -= 1
            c2 = s[j].lower()
            
            if c1 != c2:
                valid = False
                break
            
            i += 1
            j -= 1
            
        return valid