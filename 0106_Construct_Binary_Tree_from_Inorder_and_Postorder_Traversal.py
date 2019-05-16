# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # find root first, usually us not inorder to find the root.
        if len(inorder) == 0:
            return None
        root = postorder[-1]
        root_index = inorder.index(root)
        root = TreeNode(root)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:len(postorder)-1])
        return root