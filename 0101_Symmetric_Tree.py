# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursively
        # check current node with check (cur.left, cur.right)
        # then check (cur.left.right, cur.right.left) and (cur.left.left, cur.right.right)
        def isSymmetricHelper(l, r) -> bool:
            if l == None and r == None:
                return True
            elif l == None or r == None:
                return False
            if l.val != r.val:
                return False
            return isSymmetricHelper(l.right, r.left) and isSymmetricHelper(l.left, r.right)
            
        if root == None: return True
        return isSymmetricHelper(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # iteratively
        # use stack to compare (right, left) and then (right.left, left.right) and (right.right, left.left)
        if root == None: return True
        stack = [root.left, root.right]
        while len(stack) > 0:
            r = stack.pop()
            l = stack.pop()
            if r == None and l == None:
                continue
            elif r == None or l == None:
                return False
            if r.val != l.val:
                return False
            stack.append(l.right)
            stack.append(r.left)
            stack.append(l.left)
            stack.append(r.right)
        return True