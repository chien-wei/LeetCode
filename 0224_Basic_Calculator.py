class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        #print(s)
        tokens = re.findall('\d+|[-()+*]', s)
        tokens.insert(0, '(')
        tokens.append(')')
        #print(tokens)
        stack = []
        i = 0
        while i < len(tokens):
            #print(tokens[i])
            if tokens[i] == ')':
                t = stack.pop()
                stack2 = []
                while t != '(':
                    stack2.append(t)
                    t = stack.pop()
                val = 0
                e = stack2.pop()
                if len(stack2) == 0:
                    val = int(e)
                while len(stack2) > 0:
                    #print(stack2)
                    if e == '+':
                        val = val + int(stack2.pop())
                    elif e == '-':
                        val = val - int(stack2.pop())
                    else:
                        val = int(e)
                    if len(stack2) > 0:
                        e = stack2.pop()
    
                stack.append(str(val))
            else:
                stack.append(tokens[i])
            i += 1
            #print(stack)
        #print(stack)
        return int(stack.pop())