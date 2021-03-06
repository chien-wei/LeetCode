# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nstack = []
        cur = root
        while cur:
            self.nstack.append(cur)
            cur = cur.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if len(self.nstack) > 0:
            cur = self.nstack.pop()
            res = cur.val
            if cur.right:
                cur = cur.right
                while cur:
                    self.nstack.append(cur)
                    cur = cur.left
            return res
                    
            
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.nstack) != 0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()