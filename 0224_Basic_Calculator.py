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


""" Solution 2: Pratt Parser: Top-Down Operator Precedence parsing"""

import re
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Pratt Parser: Top-Down Operator Precedence parsing
        # For more details see https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing
        
        # TDOP
        def expression(rbp=0):
            t = self.token
            self.token = next(self.token_gen)
            left = t.nud()
            while rbp < self.token.lbp:
                t = self.token
                self.token = next(self.token_gen)
                left = t.led(left)
            return left
        
        def tokenize(program):
            for token in re.findall('\d+|[-+()]', program):
                if token.isdigit():
                    yield number_token(token)
                elif token == "+":
                    yield operator_add_token()
                elif token == "-":
                    yield operator_neg_token()
                elif token == '(':
                    yield operator_lparen_token()
                elif token == ')':
                    yield operator_rparen_token()
                else:
                    raise SyntaxError('unknown operator: %s', token)
            yield end_token()
            
        def parse(program):
            self.token_gen = tokenize(program)
            self.token = next(self.token_gen)
            return expression()     
        
        # handle parentheses
        def match(tok=None):
            if tok and tok != type(self.token):
                raise SyntaxError('Expected {}'.format(tok))
            self.token = next(self.token_gen)
        
        class number_token(object):
            def __init__(self, value):
                self.value = int(value)
            def nud(self):
                return self.value
        
        class operator_add_token(object):
            lbp = 20
            def led(self, left):
                right = expression(20)
                return left + right
        class operator_neg_token(object):
            lbp = 20
            def led(self, left):
                return left - expression(20)
            
        class operator_lparen_token(object):
            lbp = 0
            def nud(self):
                expr = expression()
                match(operator_rparen_token)
                return expr
    
        class operator_rparen_token(object):
            lbp = 0
        
        class end_token(object):
            lbp = 0
            
        return parse(s.strip())