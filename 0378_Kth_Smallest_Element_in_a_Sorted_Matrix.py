class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = []
        for i in range(len(matrix)):
            heapq.heappush(queue, [matrix[i][0], i, 0])
        count = 0
        res = 0
        while k > count and queue:
            top = heapq.heappop(queue)
            count += 1
            res = top[0]
            if len(matrix[top[1]]) > top[2]+1:
                heapq.heappush(queue, [matrix[top[1]][top[2]+1], top[1], top[2]+1])
        return res