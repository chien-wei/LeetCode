class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        stat = 0
        for s in S:
            if s == '(':
                stat += 1
                if stat != 1:
                    result.append(s)
            elif s == ')':
                stat -= 1
                if stat != 0:
                    result.append(s)
            
        return ''.join(result)