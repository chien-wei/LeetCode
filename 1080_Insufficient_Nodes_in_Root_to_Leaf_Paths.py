# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        # postorder
        # when the node is leaf return accumulate number
        # if the number < limit, node.left/right = None
        # corner case: one node, use zombie
        def removeInsufficient(root, acc):
            acc += root.val
            if root.left == None and root.right == None:
                return acc
            res = float('-inf')
            if root.left:
                lacc = removeInsufficient(root.left, acc)
                if lacc < limit:
                    root.left = None
                else: res = max(res, lacc)
            if root.right:
                racc = removeInsufficient(root.right, acc)
                if racc < limit:
                    root.right = None
                else: res = max(res, racc)
            return res
        
        zombie = TreeNode(0)
        zombie.left = root
        removeInsufficient(zombie, 0)
        return zombie.left