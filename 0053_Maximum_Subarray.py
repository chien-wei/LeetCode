class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# 2019/01/10:
# explain this with function mx(i, j)  
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = 0
        acc_ind = (0, 0)
        acc_val = -float('Inf')
        mx_val = acc_val
        
        if len(nums) < 1:
            return None
        
        while end < len(nums):
            if end == 0:
                acc_val = max(acc_val, nums[0])
            else:
                acc_val += nums[end]
                if nums[end] > acc_val:
                    acc_val = nums[end]
                    start = end
                acc_ind = (start, end)

            end += 1
            mx_val = max(mx_val, acc_val)
        return mx_val