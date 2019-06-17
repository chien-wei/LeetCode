class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i >= 2 and num == nums[i-1] and num == nums[i-2]:
                continue
            nums[i] = num
            i += 1
        return i