# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def traverse(cur: TreeNode, acc: str, res: list): 
            if not cur.left and not cur.right:
                res.append(acc + str(cur.val))
                return
            if cur.left:
                traverse(cur.left, acc + str(cur.val) + "->", res)
            if cur.right:
                traverse(cur.right, acc + str(cur.val) + "->", res)
                
        res = [] # res = ["1 -> 2 ...", ...]
        if root:
            traverse(root, "", res)
        return res