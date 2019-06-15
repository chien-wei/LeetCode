# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(cur, mx, mn, res):
            res[0] = max(res[0], abs(mx - cur.val), abs(mn - cur.val))
            mn = min(mn, cur.val)
            mx = max(mx, cur.val)
            if cur.left:
                helper(cur.left, mx, mn, res)
            if cur.right:
                helper(cur.right, mx, mn, res)
        
        res = [0]
        helper(root, root.val, root.val, res)
        return res[0]