"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # just use bfs from left to right
        if not root:
            return None
        queue = [root]
        while len(queue) > 0:
            new_queue = []
            for i, q in enumerate(queue):
                if i+1 < len(queue):
                    queue[i].next = queue[i+1]
                if q.left:
                    new_queue.append(q.left)
                if q.right:
                    new_queue.append(q.right)
            queue = new_queue
        return root