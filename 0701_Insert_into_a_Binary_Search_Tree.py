# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(cur: TreeNode, val: int):
            if val > cur.val:
                if cur.right:
                    helper(cur.right, val)
                else:
                    cur.right = TreeNode(val)
                    return
            else:
                if cur.left:
                    helper(cur.left, val)
                else:
                    cur.left = TreeNode(val)
                    return
            return
        
        if not root:
            root = TreeNode(val)
        else: 
            helper(root, val)
        return root