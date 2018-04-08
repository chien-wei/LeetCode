# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        return self.recur(root)
        
    def recur(self, root):
        if root.left:
            root.left = self.recur(root.left)
        if root.right:
            root.right = self.recur(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root