class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        
        ans = 0
        mx, sec = -1, -1
        for i, num in enumerate(nums):
            if num > mx:
                mx, sec = num, mx
                ans = i
            else:
                sec = max(sec, num)
        return ans if mx >= sec * 2 else -1