class Solution:
    def isValid(self, S: str) -> bool:
        # stack
        stack = []
        i = 0
        for c in S:
            stack.append(c)
            i += 1
            if len(stack) >= 3 and c == 'c' and "".join(stack[i-3:]) == "abc":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    i -= 3
            
        if len(stack) == 0:
            return True
        return False