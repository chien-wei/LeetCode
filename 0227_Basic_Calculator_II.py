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
            for token in re.findall('\d+|[-+*/]', program):
                if token.isdigit():
                    yield number_token(token)
                elif token == "+":
                    yield operator_add_token()
                elif token == "-":
                    yield operator_neg_token()
                elif token == "*":
                    yield operator_mul_token()
                elif token == "/":
                    yield operator_div_token()
                else:
                    raise SyntaxError('unknown operator: {}'.format(token))
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
            
        class operator_mul_token(object):
            lbp = 30
            def led(self, left):
                return left * expression(30)
            
        class operator_div_token(object):
            lbp = 30
            def led(self, left):
                return left // expression(30)
        
        class end_token(object):
            lbp = 0
            
        return parse(s.strip())