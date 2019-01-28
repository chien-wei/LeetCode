# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        cur = root
        while cur.left or cur.right:
            if cur.left:
                tmp = cur.right
                cur.right = cur.left
                cur.left = None
                right_most = cur.right
                while right_most.right:
                    right_most = right_most.right
                right_most.right = tmp
            cur = cur.right
