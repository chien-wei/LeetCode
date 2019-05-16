class Solution:
    def minWindow(self, s: str, t: str) -> str:
        require = {}
        for e in t:
            require[e] = require.get(e, 0) + 1
        
        start, end = 0, 1
        ans = s
        found = False
        while end < len(s)+1:
            if s[end-1] in require:
                    require[s[end-1]] -= 1
            while len(list(filter(lambda x: require[x] > 0, require))) == 0 and start < end:
                found = True
                if end - start < len(ans):
                    ans = s[start:end]
                
                if s[start] in require:
                    require[s[start]] += 1
                start += 1
            end += 1
                
        return ans if found else ""