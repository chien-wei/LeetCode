# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lf = []
        rf = [root]
        zigzagorder = []
        while len(lf) > 0 or len(rf) > 0:
            if len(lf) > 0:
                tmp = []
                while len(lf) > 0:
                    if lf[-1].right:
                        rf.append(lf[-1].right)
                    if lf[-1].left:
                        rf.append(lf[-1].left)
                    tmp.append(lf.pop().val)
                zigzagorder.append(tmp)
            if len(rf) > 0:
                tmp = []
                while len(rf) > 0:
                    if rf[-1].left:
                        lf.append(rf[-1].left)
                    if rf[-1].right:
                        lf.append(rf[-1].right)
                    tmp.append(rf.pop().val)
                zigzagorder.append(tmp)
        return zigzagorder