# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # All about binary search, find top point first
        # find left side and right side for target
        N = mountain_arr.length()
        lo, mi, hi = 0, (N-1) // 2, N-1
        i = mi
        l, m, r = mountain_arr.get(i-1), mountain_arr.get(i), mountain_arr.get(i+1)
        while m < l or m < r:
            if l < r:
                lo = mi+1
            else:
                hi = mi
            mi = (lo + hi) // 2
            i = mi
            l, m, r = mountain_arr.get(i-1), mountain_arr.get(i), mountain_arr.get(i+1)
        
        MI = mi
        # find left side first
        lo, hi = 0, MI
        mi = (lo + hi) // 2
        while lo < hi:
            if mountain_arr.get(mi) < target:
                lo = mi + 1
            else:
                hi = mi
            mi = (lo + hi) // 2
                
        if mountain_arr.get(mi) == target:
            return mi
        
        # find right side
        lo, hi = MI+1, N-1
        mi = (lo + hi) // 2
        while lo < hi:
            if mountain_arr.get(mi) > target:
                lo = mi + 1
            else:
                hi = mi
            mi = (lo + hi) // 2
                
        if mountain_arr.get(mi) == target:
            return mi
        return -1