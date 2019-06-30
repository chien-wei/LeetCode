class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def helper(s, i, j):
            bools = [[]]
            level = 0
            start = 0
            for k in range(i, j):
                if s[k] == "(":
                    if level == 0:
                        start = k + 1
                    level += 1
                elif level == 0 and s[k] == "t":
                    bools[-1].append(True)
                elif level == 0 and s[k] == "f":
                    bools[-1].append(False)
                elif s[k] == "," and level == 0:
                    bools.append([])
                elif s[k] == ")":
                    level -= 1
                    if level == 0:
                        bools[-1].append(helper(s, start, k))
                
            bs = [val for sublist in bools for val in sublist]
            op = s[i - 2] if i > 1 else ""
            if op == "":
                return bs
            elif op == "!":
                return not bs[0]
            elif op == "&":
                return all(bs)
            elif op == "|":
                return any(bs)
        return helper(expression, 0, len(expression))[0]