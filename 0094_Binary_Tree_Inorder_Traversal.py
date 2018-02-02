# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        inorder = []
        while len(stack) > 0:
            if stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None
            else:
                tmp = stack.pop()
                inorder.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
        return inorder