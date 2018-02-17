# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        stack = [(root, 1)] # elements in stack is tuple(TreeNode, depth)
        while stack:
            top = stack.pop()
            depth = max(depth, top[1])
            if top[0].left:
                stack.append((top[0].left, top[1]+1))
            if top[0].right:
                stack.append((top[0].right, top[1]+1))
        return depth