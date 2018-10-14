class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        while '()' in S:
            S = ''.join(S.split('()'))
            
        return len(S)