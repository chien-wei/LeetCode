class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for d in path:
            if d == '.' or d == ' ' or d == '':
                continue
            elif d == '..' and len(stack) > 0:
                stack.pop()
            elif d == '..':
                continue
            else:
                stack.append(d)
        
        if len(stack) == 0:
            return '/'
        result = ''
        for d in stack:
            result += '/' + d
        return result