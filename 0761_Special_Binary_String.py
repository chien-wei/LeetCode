# The idea of this solution based on alexander's article:
# https://discuss.leetcode.com/topic/116419/think-of-it-as-valid-parentheses


class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        self.i = 0
        
        def dfs(S):
            result = ''
            toks = []
            while self.i < len(S) and len(result) == 0:
                if S[self.i] == '1':
                    self.i += 1
                    toks.append(dfs(S))
                else:
                    self.i += 1
                    result += '1'
            prefix = (False, True)[len(result) > 0]
            toks = sorted(toks)[::-1]
            result += str.join('', toks)
            if prefix:
                result += '0'
            return result
        
        return dfs(S)