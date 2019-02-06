# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        infix = []
        
        def traversal(root, infix):
            if not root:
                return None
            l = traversal(root.left, infix) 
            if l != None:
                infix.append(l)
            infix.append(root.val)
            r = traversal(root.right, infix)
            if r != None:
                infix.append(r)
            #print(infix)
                
        traversal(root, infix)
        return infix[k-1]

# Follow up: What if the BST change often?
# We could add the count number for each node.
