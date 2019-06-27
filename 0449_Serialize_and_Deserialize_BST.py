# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# BFS and binary tree index: TLE
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # use bfs
        if root == None:
            return "[]"
        que = []
        que.append(root)
        res = []
        while any(que):
            next_level = []
            while len(que) > 0:
                cur = que.pop(0)
                if cur == None:
                    res.append(None)
                    next_level.append(None)
                    next_level.append(None)
                else:
                    res.append(str(cur.val))
                    next_level.append(cur.left if cur.left else None)
                    next_level.append(cur.right if cur.right else None)
            
            que = next_level
        while res[-1] == None:
            res.pop()
        return "[" + ",".join(list(map(lambda x: x if x != None else "null", res))) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # use tree index 2n+1, 2n+2
        if data == "[]":
            return None
        lis = data[1:len(data)-1].split(",")
        if len(lis) == 0:
            return None
        lis = list(map(lambda x: TreeNode(int(x)) if x != "null" else None, lis))
        N = len(lis)
        
        for i in range(N):
            if lis[i] == None:
                continue
            left, right = 2 * i + 1, 2 * i + 2
            if left < N and lis[left] != None:
                lis[i].left = lis[left]
            if right < N and lis[right] != None:
                lis[i].right = lis[right]
        return lis[0]


# preorder and inorder: Accepted
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        vals = []
        preorder(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)