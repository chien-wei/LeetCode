# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        seen = []
        stack = [root]
        while stack:
            seen.append(stack[-1].val)
            top = stack.pop()
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
                
        ans = float('inf')
        seen = sorted(seen)
        for i in range(len(seen)-1):
            ans = min(ans, seen[i+1] - seen[i])
        return ans
