# union find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = {}
        for i in range(2001):
            parent[i] = i
        
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
                
        for e in edges:
            find1 = find(e[0])
            find2 = find(e[1])
            if find1 == find2:
                return e
            elif find1 != find2:
                parent[find1] = find2