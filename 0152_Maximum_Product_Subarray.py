class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        mx = [float('-inf')] * N
        mn = [float('inf')] * N
        ans = float('-inf')
        for i, num in enumerate(nums):
            if i > 0 and num >= 0:
                mx[i] = max(num, mx[i-1] * num)
                mn[i] = min(num, mn[i-1] * num)
            elif i > 0 and num < 0:
                mx[i] = max(num, mn[i-1] * num)
                mn[i] = min(num, mx[i-1] * num)
            else:
                mx[i] = num
                mn[i] = num
            ans = max(ans, mx[i])
        return ans