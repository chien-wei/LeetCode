# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [root]
        res = []
        while len(queue) > 0:
            nxt_queue = []
            level = []
            while len(queue) > 0:
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    nxt_queue.append(cur.left)
                if cur.right:
                    nxt_queue.append(cur.right)
            res.insert(0, level)
            queue = nxt_queue
        return res