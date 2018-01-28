class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            length = len(stack)
            if c is ')' and length > 0:
                if stack.pop() is not '(':
                    return False
            elif c is ']' and length > 0:
                if stack.pop() is not '[':
                    return False
            elif c is '}' and length > 0:
                if stack.pop() is not '{':
                    return False
            else:
                stack.append(c)
        if len(stack) == 0: 
            return True
        return False