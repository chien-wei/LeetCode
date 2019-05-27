from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def backtrack(n, i, acc, acc_product, res):
            if acc_product == n:
                res.append(acc)
                return
            for j in range(i, n):
                if n // acc_product % j == 0:
                    acc.append(j)
                    acc_product *= j
                    backtrack(n, j, acc[:], acc_product, res)
                    acc_product /= j
                    acc.pop()

        res = []
        if n == 1:
            return res
        backtrack(n, 2, [], 1, res)
        return res

s = Solution()
print(s.getFactors(32))
print(s.getFactors(12))
print(s.getFactors(37))
print(s.getFactors(1))

        