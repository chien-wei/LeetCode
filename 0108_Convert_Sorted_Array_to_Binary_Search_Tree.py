# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def list2tree(nums):
            if len(nums) == 0:
                return None
            elif len(nums) == 1:
                return TreeNode(nums[0])
            mi = len(nums)//2
            l1, l2 = nums[:mi], nums[mi+1:]
            t = TreeNode(nums[mi])
            t.left = list2tree(l1)
            t.right = list2tree(l2)
            return t
        return list2tree(nums)
