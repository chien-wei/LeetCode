class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, -float('inf')
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum