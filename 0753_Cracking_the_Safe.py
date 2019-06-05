class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # use dfs to try every number
        # use map to keep visited password
        # if revisit happens, then the answer is not shortest
        
        def dfs(n, k, visited, cur, ans):
            if len(visited) == k ** n:
                return ans
            
            for j in range(k):
                newcur = cur[1:] + str(j)
                if newcur in visited:
                    continue
                visited.add(newcur)
                tmp = dfs(n, k, visited, newcur, ans + str(j))
                if tmp != None:
                    return tmp
                visited.remove(newcur)
            return None
        
        # I wrote set(init) and the set was set('0') not set("000...")
        init = "0" * n
        visited = set()
        visited.add(init)
        return dfs(n, k, visited, init, init)