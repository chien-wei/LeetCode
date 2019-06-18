class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1] * N
        acc = 1
        for i in range(1, N):
            acc *= nums[i-1]
            left[i] = acc
        acc = 1
        # right
        for j in range(N-2, -1, -1):
            acc *= nums[j+1]
            left[j] *= acc
        return left