class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        level, water = 0, 0
        while r > l:
            lower = min(height[l], height[r])
            if (height[r] > height[l]):
                l += 1
            else:
                r -= 1
            level = max(level, lower)
            water += level - lower
        return water