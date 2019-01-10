# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

# 2019/01/10
        def check(p, q):
            if type(p) != type(q) or (p and q and p.val != q.val):
                return False
            ans = True
            if p:
                ans = ans and check(p.left, q.left) 
            if q:
                ans = ans and check(p.right, q.right)
            return ans
                
            
        return check(p, q)