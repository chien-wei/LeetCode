class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return 0
        stack = []
        for t in tokens:
            if t == '+':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 + n2)
            elif t == '-':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif t == '*':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 * n2)
            elif t == '/':
                n2 = stack.pop()
                n1 = stack.pop()
                if n1 * n2 < 0 and n1 % n2 != 0:
                    stack.append(n1//n2 + 1)
                else:
                    stack.append(n1 // n2)
            else:
                stack.append(int(t))
        return stack[0]