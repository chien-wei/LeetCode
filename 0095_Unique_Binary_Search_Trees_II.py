from itertools import product
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def generate(n1, n2, dp):
            if n2 == 0:
                return []
            
            if len(dp[n1][n2]) != 0:
                return dp[n1][n2]
            if n1 == n2:
                dp[n1][n2] = [TreeNode(n1)]
                return dp[n1][n2]
            elif n2 - n1 == 1:
                t1 = TreeNode(n1)
                t1.right = TreeNode(n2)

                t2 = TreeNode(n2)
                t2.left = TreeNode(n1)
                dp[n1][n2] = [t1, t2]
                return dp[n1][n2]
            else:
                ans = []
                for i in range(n1, n2+1):
                    if i == n1:
                        for tree in generate(n1+1, n2, dp):
                            new_tree = TreeNode(i)
                            new_tree.right = tree
                            ans.append(new_tree)
                    elif i == n2:
                        for tree in generate(n1, n2-1, dp):
                            new_tree = TreeNode(i)
                            new_tree.left = tree
                            ans.append(new_tree)
                    else:
                        for (t1, t2) in product(generate(n1, i-1, dp), generate(i+1, n2, dp)):
                            new_tree = TreeNode(i)
                            new_tree.left = t1
                            new_tree.right = t2
                            ans.append(new_tree)
                dp[n1][n2] = ans
                return ans
            
        dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
        return generate(1, n, dp)