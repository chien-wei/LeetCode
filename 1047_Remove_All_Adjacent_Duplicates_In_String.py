class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] == c:
                while len(stack) > 0 and stack[-1] == c:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)