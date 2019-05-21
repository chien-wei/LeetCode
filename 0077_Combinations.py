class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(n, k, used, acc, res):
            if len(acc) == k:
                res.append(acc)
                return
            
            for i in range(acc[-1]+1 if len(acc) > 0 else 1, n+1):
                if not used[i]:
                    used[i] = True
                    acc.append(i)
                    backtrack(n, k, used, acc[:], res)
                    acc.pop()
                    used[i] = False
        
        res = []
        used = [True] + [False for _ in range(n)]
        backtrack(n, k, used, [], res)
        return res