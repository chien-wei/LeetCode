# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root, n, acc):
            if root == None:
                return None
            acc.append(root)
            if root == n:
                return acc
            l = search(root.left, n, acc[:])
            r = search(root.right, n, acc[:])
            if l != None:
                return l
            return r
            
        p_branch = search(root, p, [])
        q_branch = search(root, q, [])
        for pb in p_branch[::-1]:
            for qb in q_branch:
                if pb == qb:
                    return pb
        return root

