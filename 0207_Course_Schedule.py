class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for u in range(numCourses):
            graph[u] = []
        degree = [0 for _ in range(numCourses)]
        for [v, u] in prerequisites:
            graph[u].append(v)
            degree[v] += 1
            
        # do those with degree 0 first, BFS
        queue = []
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while len(queue) > 0:
            u = queue.pop(0)
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)
        if sum(degree) > 0:
            return False
        return True
        