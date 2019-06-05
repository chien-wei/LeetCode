# find first num[i] < num[i-1]: O(m*n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        for _ in range(k):
            i = 1
            while i+1 < len(num) and int(num[i]) >= int(num[i-1]):
                i += 1
            if int(num[i-1]) > int(num[i]):
                num = num[:i-1] + num[i:]
            else:
                num = num[:i] + num[i+1:]
            i += 1
        return str(int(num))

# stack: O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        stack = []
        i = 0
        while k > 0:
            if i == len(num):
                stack = stack[:len(stack)-k]
                break
            while len(stack) > 0 and int(num[i]) < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(int(num[i]))
            i += 1
        res = str(int("".join(map(str, stack)) + num[i:]))
        return res