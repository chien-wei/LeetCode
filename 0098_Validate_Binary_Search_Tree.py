# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def recur(root, bound):
            if root.val >= bound[0] or root.val <= bound[1]:
                return False
            res = True
            if root.left:
                res = res and recur(root.left, [root.val, bound[1]])
            if root.right:
                res = res and recur(root.right, [bound[0], root.val])
                
            return res
            
        if not root:
            return True
        return recur(root, [float('inf'), float('-inf')])