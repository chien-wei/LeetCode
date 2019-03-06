# two index for two array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        j = len(nums2) - 1
        i = len(nums1) - len(nums2) - 1
        k = len(nums1) - 1
        
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            elif i >= 0 and j >= 0 and nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            elif i >= 0:
                k -= 1
                i -= 1