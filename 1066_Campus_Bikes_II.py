# Backtracking: factorial complexity, got TLE 
from typing import List
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def backtrack(workers, bikes, i, used, acc, mn):
            print(i, used, acc, mn)
            if i == len(workers):
                mn[0] = min(mn[0], acc[0])
                return
                
            for j in range(len(bikes)):
                if not used[j]:
                    used[j] = True
                    dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                    acc[0] += dis
                    backtrack(workers, bikes, i+1, used, acc[:], mn)
                    acc[0] -= dis
                    used[j] = False
        
        mn = [float('inf')]
        backtrack(workers, bikes, 0, [False for _ in range(len(bikes))], [0], mn)
        return mn[0]

# optimize with memory: accepted, more like dfs now
# 1. We need something as key in memory: (person, used_bike) can work
# 2. Instead of pass the minimum value by reference, we keep it in each function scope so 
#    we know which one is smallest. We store that value.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def backtrack(workers, bikes, i, used, memo):
            if i == len(workers):
                return 0
            
            if (i, tuple(used)) in memo:
                return memo[(i, tuple(used))]
            
            mn = float('inf')
                
            for j in range(len(bikes)):
                if not used[j]:
                    used[j] = True
                    dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                    mn = min(mn, dis + backtrack(workers, bikes, i+1, used, memo))
                    used[j] = False
            
            memo[(i, tuple(used))] = mn
            return mn
        
        return backtrack(workers, bikes, 0, [False for _ in range(len(bikes))], {})