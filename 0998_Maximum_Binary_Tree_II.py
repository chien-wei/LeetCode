# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        tmp = TreeNode(float('inf'))
        tmp.left = root
        cur = root
        parent = tmp
        while cur and val < cur.val:
            parent, cur = cur, cur.right
            
        if cur == None:
            parent.right = TreeNode(val)
            return root
        
        parent.right = TreeNode(val)
        parent.right.left = cur
        if parent == tmp:
            return parent.right
        return root