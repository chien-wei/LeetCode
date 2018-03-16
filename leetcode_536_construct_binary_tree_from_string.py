class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        i = s.find('(')
        if i < 0:
            return TreeNode(int(s)) if s else None
        d = 0
        for j, mark in enumerate(s):
            print(j, mark)
            if mark == '(':
                d += 1
            if mark == ')':
                d -= 1
            if j > i and d == 0:
                break
        root = TreeNode(int(s[:i]))
        root.left = self.str2tree(s[i+1:j])
        root.right = self.str2tree(s[j+2:-1])
        return root


S = Solution()
print S.str2tree("4(2(3)(1))(6(5))")
