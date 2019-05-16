# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS find the first leaf
        if not root:
            return 0
        queue = [root]
        depth = 1
        while len(queue) > 0:
            new_queue = []
            for i in range(len(queue)):
                q = queue[i]
                if not q.left and not q.right:
                    return depth
                if q.left:
                    new_queue.append(q.left)
                if q.right:
                    new_queue.append(q.right)
            queue = new_queue
            depth += 1
        return 0