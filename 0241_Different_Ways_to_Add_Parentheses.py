import re
import operator
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # divide and conquer with memorization
        OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        
        tokens = re.split(r'(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map(OPS.get, tokens[1::2]))
        memo = [[[] for _ in range(len(nums))] for _ in range(len(nums))]
        
        def divide(lo: int, hi: int) -> List[int]:
            if len(memo[lo][hi]) > 0:
                return memo[lo][hi]
            if lo == hi:
                memo[lo][hi] = [nums[lo]]
                return [nums[lo]]
            res = []
            for i in range(lo, hi):
                for a in divide(lo, i):
                    for b in divide(i+1, hi):
                        res.append(ops[i](a, b))
            memo[lo][hi] = res
            return res
        return divide(0, len(nums) - 1)