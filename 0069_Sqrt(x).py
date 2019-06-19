class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mi = (lo + hi) // 2
            val = mi * mi
            if val >= x:
                hi = mi
            else:
                lo = mi + 1
        return lo - 1 if lo * lo > x else lo