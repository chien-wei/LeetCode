class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        
        def union(id1, id2, parent, group_count):
            f1 = find(id1, parent)
            f2 = find(id2, parent)
            if f1 != f2:
                parent[f1] = f2
                group_count[0] -= 1
            
        def find(idk, parent):
            if parent[idk] == idk:
                return idk
            return find(parent[idk], parent)
        
        sort = sorted(logs)
        parent = [i for i in range(N)]
        group_count = [N]
        for time, id1, id2 in sort:
            union(id1, id2, parent, group_count)
            if group_count[0] == 1:
                return time
        return -1