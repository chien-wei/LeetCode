class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        if target < nums[lo]:
            return lo
        if target > nums[hi]:
            return hi+1
        
        
        mi = (lo + hi) // 2
        last_mi = -1
        while nums[mi] != target and last_mi != mi:
            last_mi = mi
            if nums[mi] < target:
                lo = mi
            elif nums[mi] > target:
                hi = mi
            mi = (lo + hi) // 2
        if last_mi == mi:
            mi += 1
        return mi

# See how can I write directly to the following version
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return end + 1