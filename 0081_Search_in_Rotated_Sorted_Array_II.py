class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return nums[0] == target
        
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            while lo < hi and nums[lo] == nums[hi]:
                lo += 1
            mi = (lo + hi) // 2
            print(lo, hi, mi)
            if  target == nums[mi]:
                return True
            elif nums[hi] >= nums[mi]:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
                    
            else:
                if nums[mi] > target >= nums[lo]:
                    hi = mi - 1
                else:
                    lo = mi + 1
        return False