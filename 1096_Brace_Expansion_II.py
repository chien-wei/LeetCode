# keep level value and parse when level == 0
from itertools import product
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        def helper(s, i, j):
            groups = [[]]
            level = 0
            start = 0
            for k in range(i, j):
                if s[k] == "{":
                    if level == 0:
                        start = k+1
                    level += 1
                elif s[k] == "}":
                    level -= 1
                    if level == 0:
                        groups[-1].append(helper(s, start, k))
                elif s[k] == "," and level == 0:
                    groups.append([])
                elif level == 0:
                    groups[-1].append([s[k]])
                    
            word_set = set()
            for group in groups:
                word_set |= set(map(''.join, product(*group)))
            return sorted(word_set)
        
        return helper(expression, 0, len(expression))

# TODO: use functional paradiam to solve this