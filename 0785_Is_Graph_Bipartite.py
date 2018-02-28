class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        def dfs(ind):
            print(ind, color)
            for j in graph[ind]:
                if j not in color:
                    color[j] = 1 - color[ind]
                elif color[j] == color[ind]:
                    return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
            if not dfs(i):
                return False
        return True