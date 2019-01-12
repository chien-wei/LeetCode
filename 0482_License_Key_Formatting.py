class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K < 1:
            return 0
        s = S.replace('-', '')
        rest = len(s) % K
        ans = ''
        if rest != 0:
            ans += s[:rest].upper()
        else:
            rest = K
            ans += s[:rest].upper()
        while rest < len(s):
            ans += '-' + s[rest:rest+K].upper()
            rest += K
        
        return ans