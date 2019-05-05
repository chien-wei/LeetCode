# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def reverse_inorder(root: TreeNode, r: int):
            if root.right:
                r = reverse_inorder(root.right, r)
            
            l = 0
            if root.left:
                l = reverse_inorder(root.left, r + root.val)
            root.val += r
            return max(root.val, l)
        
        reverse_inorder(root, 0)
        return root
        