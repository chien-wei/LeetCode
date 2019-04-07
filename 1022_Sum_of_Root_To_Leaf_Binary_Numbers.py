# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def go(cur: TreeNode, acc: int):
            if cur.left == None and cur.right == None:
                return acc + cur.val
            elif cur.left and cur.right:
                return go(cur.left, (acc+cur.val)*2) + go(cur.right, (acc+cur.val)*2)
            elif cur.left:
                return go(cur.left, (acc+cur.val)*2)
            elif cur.right:
                return go(cur.right, (acc+cur.val)*2)
            
        return go(root, 0) % (10**9 + 7)