class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # classic xor problem
        res = 0
        for num in nums:
            res ^= num
        return res