# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def traverse(cur): # (accumulated value, number of nodes, max)
            if cur.left is None and cur.right is None:
                return (cur.val, 1, cur.val)
            la = ln = lmx = ra = rn = rmx = 0
            if cur.left is not None:
                (la, ln, lmx) = traverse(cur.left)
            if cur.right is not None:
                (ra, rn, rmx) = traverse(cur.right)
            ca = la + ra + cur.val
            cn = ln + rn + 1
            return (ca, cn, max(lmx, rmx, ca / cn))
                
        if root is None:
            return 0
        return traverse(root)[2]