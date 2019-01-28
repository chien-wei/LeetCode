# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(ino, pre):
            if len(ino) == 0:
                return None
            elif len(ino) == 1:
                return TreeNode(ino[0])

            root = pre[0]
            mi = ino.index(root)
            ino_child1 = ino[:mi]
            pre_child1 = pre[1:len(ino_child1)+1]
            ino_child2 = ino[mi+1:]
            pre_child2 = pre[mi+1:]

            t = TreeNode(root)
            t.left = helper(ino_child1, pre_child1)
            t.right = helper(ino_child2, pre_child2)
            return t

        return helper(inorder, preorder)
