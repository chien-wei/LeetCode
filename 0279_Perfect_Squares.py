# took 2300ms
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = min([dp[i - j*j] for j in range(1, int(i ** 0.5) + 1)]) + 1
        return dp[n]

# this took less
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1, # <= comma
        return dp[n]