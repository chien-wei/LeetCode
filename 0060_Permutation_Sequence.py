# use backtracking: TLE
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # use backtracking to put the result
        # use a variable to keep track of how many number of result we have
        # use a dictionary or list to keep track of usage of n
        used = [True] + [False for _ in range(n)]
        def backtrack(n, used, acc, res, k):
            if res != []:
                return
            
            if len(acc) == n:
                k[0] -= 1
                if k[0] == 0:
                    res.append(acc)
                    return
                
            for i in range(1, n+1):
                if not used[i]:
                    used[i] = True
                    backtrack(n, used, acc + str(i), res, k)
                    used[i] = False
                
        K = [k]
        res = []
        backtrack(n, used, "", res, K)
        return res[0]

# divide and conquer: Accepted
from functools import reduce
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        numbers = list(range(1, n+1))
        NN = reduce(operator.mul, numbers)
        k = (k-1) % NN
        result = ''
        while len(numbers) > 0:
            NN = NN // len(numbers)
            i, k = k // NN, k % NN
            result += str(numbers.pop(i))
        return result