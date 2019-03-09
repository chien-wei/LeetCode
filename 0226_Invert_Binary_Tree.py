# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteratively
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        nodes = [root]
        while len(nodes) > 0:
            cur = nodes.pop(0)
            if cur.right:
                nodes.append(cur.right)
            if cur.left:
                nodes.append(cur.left)
            cur.left, cur.right = cur.right, cur.left
        
        return root

# recursively
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recur(cur):
            if cur.right:
                cur.right = recur(cur.right)
            if cur.left:
                cur.left = recur(cur.left)
            cur.left, cur.right = cur.right, cur.left
            return cur
        return recur(root) if root else root