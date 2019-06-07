class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mi = (lo + hi) // 2
            if target == nums[mi]:
                return mi
            elif target > nums[mi]:
                lo = mi + 1
            else:
                hi = mi
        return -1