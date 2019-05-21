class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # use backtracking
        # from 1~9 pick numbers until we got k numbers
        # if we got k number but not reach n, stop
        # if we got n but not k number, stop
        
        def backtrack(k, n, i, acc, acc_sum, res):
            if len(acc) == k and acc_sum == n:
                res.append(acc)
                return
            elif len(acc) >= k or acc_sum >= n:
                return
            
            for j in range(i, 10):
                acc.append(j)
                acc_sum += j
                backtrack(k, n, j+1, acc[:], acc_sum, res)
                acc_sum -= j
                acc.pop()
                
        res = []
        backtrack(k, n, 1, [], 0, res)
        return res