# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def Codec(self, root: TreeNode) -> str:
        res = []
        level = deque()
        level.append(root)
        while True:
            next_level = deque()
            if any(level):
                while len(level) > 0:
                    cur = level.popleft()
                    res.append(cur.val if cur else None)
                    if cur:
                        next_level.append(cur.left if cur.left else None)
                        next_level.append(cur.right if cur.right else None)
                level = next_level
            else:
                break
        while len(res) > 0 and res[-1] == None:
            res.pop()
        return res

