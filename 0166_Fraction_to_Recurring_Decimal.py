class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return "NaN"
        res = ""
        if numerator * denominator < 0:
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            return res + str(numerator // denominator)
        res += str(abs(numerator // denominator)) + '.'
        num = numerator % denominator
        appeared = {}
        num = num * 10
        while num % denominator != 0:
            if num in appeared:
                res = res[:appeared[num]] + '(' + res[appeared[num]:] + ')'
                return res
            appeared[num] = len(res)
            q = num // denominator
            res += str(q)
            num -= q * denominator
            num *= 10
            
        return res + str(num // denominator)