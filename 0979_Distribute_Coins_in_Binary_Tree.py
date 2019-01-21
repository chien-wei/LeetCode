# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def moveCoins(root, mv):
            if not root:
                return 0
            left = moveCoins(root.left, mv)
            right = moveCoins(root.right, mv)
            mv[0] += abs(left) + abs(right)
            return root.val + left + right - 1
            
        mv = [0]
        moveCoins(root, mv)
        return mv[0]
        
        
        
        