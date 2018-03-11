class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans, [], 0, graph)
        return ans
        
    def dfs(self, ans, path, n, graph):
        path.append(n)
        if n == len(graph)-1:
            ans.append(path)
        #print(ans, path, n, graph)
        for i in graph[n]:
            #print(i)
            self.dfs(ans, path[:], i, graph)