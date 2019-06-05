class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        M, N = len(num1), len(num2)
        i, j = M-1, N-1
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                tmp = carry + int(num1[i]) + int(num2[j])
                sm, carry = tmp % 10, tmp // 10
                res = str(sm) + res
                i, j = i-1, j-1
            elif i >= 0:
                tmp = carry + int(num1[i])
                sm, carry = tmp % 10, tmp // 10
                res = str(sm) + res
                i -= 1
            elif j >= 0:
                tmp = carry + int(num2[j])
                sm, carry = tmp % 10, tmp // 10
                res = str(sm) + res
                j -= 1
        if carry > 0:
            res = str(carry) + res
        return res