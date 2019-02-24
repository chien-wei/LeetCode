class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        is_not_judge = {}
        is_trusted = {}
        for i in range(1, N+1):
            is_trusted[i] = set()
        
        for [a, b] in trust:
            is_trusted[b].add(a)
            is_not_judge[a] = True
        
        for i in range(1, N+1):
            if i not in is_not_judge and len(is_trusted[i]) == N-1:
                return i
        return -1