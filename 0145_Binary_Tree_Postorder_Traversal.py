# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        postorder = []
        while len(stack) > 0:
            if not stack[-1].left and not stack[-1].right:
                postorder.append(stack.pop().val)
            elif stack[-1].right and stack[-1].left:
                stack.append(stack[-1].right)
                stack.append(stack[-2].left)
                stack[-3].right = None
                stack[-3].left = None
            elif stack[-1].right:
                stack.append(stack[-1].right)
                stack[-2].right = None
            elif stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None
        return postorder