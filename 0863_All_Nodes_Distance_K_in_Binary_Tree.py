# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        parent_of = {}
        stack = [root]
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp.left:
                parent_of[tmp.left.val] = tmp
                stack.append(tmp.left)
            if tmp.right:
                parent_of[tmp.right.val] = tmp
                stack.append(tmp.right)
        
        seen = [target]
        cand = [target]
        for i in range(K):
            new_cand = []
            for c in cand:
                if c != root and parent_of[c.val] not in seen:
                    new_cand.append(parent_of[c.val])
                    seen.append(parent_of[c.val])
                if c.left and c.left not in seen:
                    new_cand.append(c.left)
                    seen.append(c.left)
                if c.right and c.right not in seen:
                    new_cand.append(c.right)
                    seen.append(c.right)
            cand = new_cand
        return [node.val for node in cand]