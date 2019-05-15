# Need to use Morris Traversal to achieve Space in O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # using inorder to find uncommon place in BST
        # uncommon means the element in order a, b => b < a
        # if one uncommon place is found, swap it with the previous node
        # if two uncommon place is found, just swap them
        
        def inOrder(root, l):
            if root.left != None:
                inOrder(root.left, l)
            l.append(root)
            print(l[-1].val)
            if root.right != None:
                inOrder(root.right, l)
            
        inOrderList = []
        inOrder(root, inOrderList)
        uncommon = []
        for i in range(1, len(inOrderList)):
            if inOrderList[i].val < inOrderList[i-1].val:
                uncommon.append(inOrderList[i-1])
                uncommon.append(inOrderList[i])
        
        if len(uncommon) == 2:
            uncommon[0].val, uncommon[1].val = uncommon[1].val, uncommon[0].val
        else:
            uncommon[0].val, uncommon[-1].val = uncommon[-1].val, uncommon[0].val
        
        