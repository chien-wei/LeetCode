from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # create a hash table for triangles
        # then use DFS to try all cases
        
        def dfs(cur: List[str], nxt: List[str], allow: dict) -> bool:
            if len(cur) == 1 and len(nxt) == 1:
                return True
            elif len(cur) == 1:
                return dfs(nxt, [], allow)
            
            key = (cur[0], cur[1])
            res = False
            for k in allow[key]:
                nxt.append(k)
                res = res or dfs(cur[1:], nxt, allow)
                nxt.pop()
            return res
            
            
        dic = defaultdict(list)
        for alw in allowed:
            *key, last = list(alw)
            dic[tuple(key)].append(last)
            
        if len(bottom) < 2:
            return False
        return dfs(bottom, [], dic)