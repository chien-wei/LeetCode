# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_family = []
        cur = root
        while cur:
            p_family.append(cur)
            if p.val == cur.val:
                break
            if p.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        q_family = []
        cur = root
        while cur:
            q_family.append(cur)
            if q.val == cur.val:
                break
            if q.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
                
        for pa in p_family[::-1]:
            for qa in q_family:
                if pa == qa:
                    return pa
        return root

# better
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur