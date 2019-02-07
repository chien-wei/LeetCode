from itertools import product
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        res = [""]
        for d in digits:
            res = list(map(lambda x: ''.join(x), list(product(res, letters[d]))))
        return res

# without using itertools
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        res = [""]
        for d in digits:
            new_res = []
            for r in res:
                for l in letters[d]:
                    new_res.append(r+l)
            res = new_res
        return res