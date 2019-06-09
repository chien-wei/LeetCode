from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack, used = [], Counter()
        for c in s:
            count[c] -= 1
            used[c] += 1
            if used[c] > 1:
                continue
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                used[stack[-1]] = 0
                stack.pop()
            stack.append(c)
        return ''.join(stack)