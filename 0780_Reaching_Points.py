class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > 0 and ty > 0:
            if (sx, sy) == (tx, ty):
                return True
            if tx == ty or sx > tx or sy > ty:
                return False
            if tx > sx and ty > sy:
                (tx, ty) = (tx-ty, ty) if tx >= ty else (tx, ty-tx)
            elif tx > sx:
                return False if (sx - tx)%ty != 0 else True
            elif ty > sy:
                return False if (sy - ty)%tx != 0 else True
                
        return False