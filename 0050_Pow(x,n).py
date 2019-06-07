class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x: float, n: int) -> float:
            res = 0
            if n < 0:
                res = recur(1/x, -n)
            elif n == 0:
                res = 1
            elif n == 1:
                res = x
            else:
                tmp = recur(x, n//2)
                res = tmp * tmp * recur(x, n % 2)
            return res
        return recur(x, n)