# backtracking for two condition: need to use seen
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(candidates, i, target, acc, res, seen):
            if (i, target, tuple(acc)) in seen:
                return
            seen[(i, target, tuple(acc))] = True
            # print(i, target, acc)
            if target == 0:
                res.append(acc) 
                return
            
            if target >= candidates[i]:
                acc.append(candidates[i])
                backtrack(candidates, i, target-candidates[i], acc[:], res, seen)
                acc.pop()
            if i+1 < len(candidates):
                backtrack(candidates, i+1, target, acc[:], res, seen)
                
            
        res = []
        backtrack(candidates, 0, target, [], res, {})
        return list(res)

