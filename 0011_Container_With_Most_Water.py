class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        mx = 0
        while j > i:
            mx = max(mx, min(height[i], height[j]) * (j - i) )
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return mx