class Solution:
    def numWays(self, n: int, k: int) -> int:
        # if same, next fence has to be different
        # if diff, next fence can be same or different
        # there are always k-1 for different
        if n == 0:
            return 0
        elif n == 1:
            return k
        same, diff = 0, k
        for i in range(n-1):
            same, diff = diff, (diff + same) * (k-1)
        return same + diff


s = Solution()
assert s.numWays(2, 4) == 16
assert s.numWays(3, 2) == 6