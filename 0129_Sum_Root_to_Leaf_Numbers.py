# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(cur: TreeNode, acc: str) -> int:
            if not cur.left and not cur.right:
                return int(acc + str(cur.val))
            l, r = 0, 0
            if cur.left:
                l = helper(cur.left, acc + str(cur.val))
            if cur.right:
                r = helper(cur.right, acc + str(cur.val))
            return l + r
        return helper(root, "") if root else 0