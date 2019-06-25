class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for n in preorder.split(','):
            stack.append(n)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False

# 2019/06/24 Getting better! O(1) space.
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # root has two child
        # whenever a child comes, a place was taken, meanwhile, one place more for another child
        count = 1
        nodes = preorder.split(",")
        for i, n in enumerate(nodes):
            if n != "#":
                count += 1
            else:
                count -= 1
            if count <= 0 and i != len(nodes) - 1:
                return False
        if count != 0:
            return False
        return True