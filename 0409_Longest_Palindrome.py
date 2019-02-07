class Solution:
    def longestPalindrome(self, s: 'str') -> 'int':
        odd = False
        count = {}
        res = 0
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in count:
            if count[c] % 2 == 0:
                res += count[c]
            else:
                res += count[c] - 1
                odd = True
        
        if odd:
            res += 1
        
        return res