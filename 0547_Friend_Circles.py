# union find
class Solution:
    def findCircleNum(self, M: 'List[List[int]]') -> 'int':
        def find(i, parent):
            if parent[i] == i:
                return i
            return find(parent[i], parent)
            
        def union(i, j, parent, group):
            find1 = find(i, parent)
            find2 = find(j, parent)
            if find1 != find2:
                parent[find1] = find2
                group -= 1
            return group
        
        parent = {}
        group = len(M)
        for i in range(len(M)):
            parent[i] = i
        
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    group = union(i, j, parent, group)
        return group