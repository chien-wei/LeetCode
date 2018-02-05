class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        stack = []
        res = []
        for i in range(len(nums2)):
            h[nums2[i]] = -1
            while stack and nums2[stack[-1]] < nums2[i]:
                h[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        for n in nums1:
            res.append(h[n])
        return res

# There is also an one-line Solution
# return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]