# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def countDepth(root, acc, valid):
            if not root:
                return (acc, True)
            (dl, vl) = countDepth(root.left, acc+1, True)
            (dr, vr) = countDepth(root.right, acc+1, True)
            if vl and vr and abs(dl - dr) <= 1:
                return (max(dl, dr), True)
            return (max(dl, dr), False)
        
        (depth, valid) = countDepth(root, 0, True)
        return valid
