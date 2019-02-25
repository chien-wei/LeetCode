class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cur_sum = 0
        for n in nums:
            if n == 1:
                cur_sum += 1
                mx = max(mx, cur_sum)
            elif n == 0:
                cur_sum = 0
        return mx