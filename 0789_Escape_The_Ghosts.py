class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tx, ty = target[0], target[1]
        td = abs(tx) + abs(ty)
        for ghost in ghosts:
            x = target[0] - ghost[0]
            y = target[1] - ghost[1]
            if (abs(x) + abs(y)) <= td:
                return False
        return True