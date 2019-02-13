class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        degree = [0 for _ in range(numCourses)]
        
        for [v, u] in prerequisites:
            graph[u].append(v)
            degree[v] += 1
        
        queue = []
        for v in range(numCourses):
            if degree[v] == 0:
                queue.append(v)
        res = []
        while len(queue) > 0:
            u = queue.pop(0)
            res.append(u)
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)
        if sum(degree) > 0:
            return []
        return res
            