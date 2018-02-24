# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# optimal structure
# This will get TLE
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l, r = root.left, root.right
        l13 = root.val
        l2 = self.rob(l) + self.rob(r)
        if l:
            ll, lr = l.left, l.right
            l13 += self.rob(ll) + self.rob(lr)
        if r:
            rl, rr = r.left, r.right
            l13 += self.rob(rl) + self.rob(rr)
        return max(l13, l2)

# optimal structure + overlapping of subproblems
class Solution:
    def __init__(self):
        self.d = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root in self.d:
            return self.d[root]
        if not root:
            return 0
        l, r = root.left, root.right
        l13 = root.val
        l2 = self.rob(l) + self.rob(r)
        if l:
            ll, lr = l.left, l.right
            l13 += self.rob(ll) + self.rob(lr)
        if r:
            rl, rr = r.left, r.right
            l13 += self.rob(rl) + self.rob(rr)
        self.d[root] = max(l13, l2)
        return self.d[root]


# https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
# The better solution is to return two value in helper function
# the values mean not robbed and robbed

class Solution:
    def robSub(self, root):
        if not root:
            return [0, 0]
        left = self.robSub(root.left)
        right = self.robSub(root.right)
        res1, res2 = max(left) + max(right), root.val + left[0] + right[0]
        return res1, res2
        
    def rob(self, root):
        res1, res2 = self.robSub(root)
        return max(res1, res2)