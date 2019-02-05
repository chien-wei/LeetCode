
class Solution:
    def closestValue(self, root, target):
        closest = float('inf')

        while root:
            if root.val == target:
                return target
            elif abs(closest - target) > abs(root.val - target):
                closest = root.val

            if target > root.val:
                root = root.right
            elif target < root.val:
                root = root.left



