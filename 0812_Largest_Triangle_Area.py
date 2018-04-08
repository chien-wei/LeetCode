class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import math
        if len(points) < 3:
            return 0
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a = math.sqrt((points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]))
                    b = math.sqrt((points[i][0] - points[k][0]) * (points[i][0] - points[k][0]) + (points[i][1] - points[k][1]) * (points[i][1] - points[k][1]))
                    c = math.sqrt((points[j][0] - points[k][0]) * (points[j][0] - points[k][0]) + (points[j][1] - points[k][1]) * (points[j][1] - points[k][1]))
                    p = (a+b+c)/2
                    tmp = p*(p-a)*(p-b)*(p-c)
                    if tmp > 0 :
                        ans = max(ans, math.sqrt(tmp))
        return ans