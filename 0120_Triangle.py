class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        N = len(triangle)
        M = N-1
        # M is length of upper row
        for i in range(1, N)[::-1]:
            for j in range(M):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
            M -= 1
        return triangle[0][0]