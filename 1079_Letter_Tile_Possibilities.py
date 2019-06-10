class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # either take or not take, dfs with used list
        # result store in set
        # the len of set -1 is the result (remove empty "")
        # get TLE, use memo
        
        def dfs(tiles, used, acc, res, memo):
            if (acc, tuple(used)) in memo:
                return
            memo[(acc, tuple(used))] = True
            
            if all(used):
                res.add(acc)
            
            for i in range(len(tiles)):
                if not used[i]:
                    used[i] = True
                    dfs(tiles, used, acc, res, memo)
                    dfs(tiles, used, acc + tiles[i], res, memo)
                    used[i] = False
            
        res = set()
        dfs(tiles, [False for _ in range(len(tiles))], "", res, {})
        return len(res)-1