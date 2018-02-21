# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, 0)]
        while stack:
            top = stack.pop()
            if not top[0].left and not top[0].right and (top[0].val + top[1]) == sum:
                return True
            if top[0].left:
                stack.append((top[0].left, top[1] + top[0].val))
            if top[0].right:
                stack.append((top[0].right, top[1] + top[0].val))
        return False