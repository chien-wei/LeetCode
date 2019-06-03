class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        
        lo = 0
        hi = len(nums)-1
        
        if nums[lo] == target:
                return lo
        if nums[hi] == target:
                return hi
        
        while lo < hi:
            mi = (hi+lo) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] > nums[lo] and target > nums[lo] and target < nums[mi]:
                hi = mi
            elif nums[mi] > nums[lo]:
                lo = mi+1
            elif nums[mi] < nums[lo] and target > nums[mi] and target < nums[hi]:
                lo = mi+1
            else:
                hi = mi
                
            if nums[lo] == target:
                return lo
            
        return -1