from collections import Counter
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        # count all char in text with Counter
        # iterate over each char again, append result at stack
        # track used
        # if char is smaller and there are other stack[-1] behind
        # discard stack[-1] from stack
        count = Counter(text)
        stack, used = [], Counter()
        for c in text:
            count[c] -= 1
            used[c] += 1
            if used[c] > 1:
                continue
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                used[stack[-1]] = 0
                stack.pop()
            stack.append(c)
        return ''.join(stack)