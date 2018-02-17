# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(root, [])] # stack store tuple of (root, curPath)
        paths = [] # store all paths
        while stack:
            top = stack.pop()
            if not top[0].left and not top[0].right:
                paths.append([*top[1], top[0].val])
            if top[0].left:
                stack.append((top[0].left, [*top[1], top[0].val]))
            if top[0].right:
                stack.append((top[0].right, [*top[1], top[0].val]))
                
        return list(filter(lambda path: sum(path) == _sum, paths))