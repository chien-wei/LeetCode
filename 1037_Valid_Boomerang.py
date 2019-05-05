class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        sorted_point = sorted(points)
        p0 = sorted_point[0]
        p1 = sorted_point[1]
        p2 = sorted_point[2]
        if p0 == p1 or p1 == p2:
            return False
        if p0[0] == p1[0] == p2[0] or p0[1] == p1[1] == p2[1]:
            return False
        if (p1[0] - p0[0]) / (p1[1] - p0[1] + 0.000001) == (p2[0] - p1[0]) / (p2[1] - p1[1] + 0.000001):
            return False
        
        return True