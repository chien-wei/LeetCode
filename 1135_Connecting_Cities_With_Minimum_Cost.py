class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # Union Find
        # First sort the connections by weights
        def union(a, b, parents):
            fa = find(a, parents)
            fb = find(b, parents)
            if fa != fb:
                parents[fb] = fa
                return True
            return False
        
        def find(n, parents):
            while parents[n] != n:
                n = parents[n]
            return n
        
        parents = [n for n in range(N+1)]
        connections.sort(key=lambda x: x[2])
        numOfUnion = N
        ans = 0
        for a, b, w in connections:
            if union(a, b, parents):
                ans += w
                numOfUnion -= 1
        return ans if numOfUnion == 1 else -1