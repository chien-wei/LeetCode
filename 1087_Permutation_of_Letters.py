import re
class Solution:
    def permute(self, S: str) -> List[str]:
        def backtrack(elements, i, acc, res):
            if i == len(elements):
                res.append(acc)
                return
            
            for j in range(len(elements[i])):
                backtrack(elements, i+1, acc + elements[i][j], res)
            
        stack = [] # S = "{a,b}c{d,e}f", stack = [[a,b],[c],[d,e],[f]]
        tokens = re.split(r'(\{|\}|,)', S)
        
        for token in tokens:
            if token == "" or token == ",":
                continue
            elif token == "}":
                sublist = []
                while stack[-1] != ["{"]:
                    sublist = stack.pop() + sublist
                stack.pop()
                stack.append(sublist)
            else:
                stack.append([token])
                
        res = []
        backtrack(stack, 0, "", res)
        return sorted(res)