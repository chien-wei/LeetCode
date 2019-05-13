# Accepted: Backtracking
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, i, target, acc, res):
            if target == 0:
                res.add(tuple(acc))
                return
            if i >= len(candidates):
                return
            
           
            backtrack(candidates, i+1, target, acc[:], res)    
            #print(i, candidates[i], target, acc)
            if target >= candidates[i]:
                acc.append(candidates[i])
                backtrack(candidates, i+1, target-candidates[i], acc[:], res)
                acc.pop()
                
            
        res = set()
        backtrack(sorted(candidates), 0, target, [], res)
        return list(res)

# TODO: DP and DFS solution