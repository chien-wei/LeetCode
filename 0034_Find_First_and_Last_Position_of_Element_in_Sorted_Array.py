class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsearch(nums: List[int], target: int):
            # find the first target encounter in nums
            # if not found, the return is the first encounter larger that target
            lo, hi = 0, len(nums)
            while lo < hi:
                mi = (lo + hi) // 2
                if target > nums[mi]:
                    lo = mi + 1
                else:
                    hi = mi
            return lo 
        
        if len(nums) == 0:
            return [-1, -1]
        first = bsearch(nums, target)
        if first >= len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, first + bsearch(nums[first:], target+1) - 1]