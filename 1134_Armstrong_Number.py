class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        ans = 0
        for n in str(N):
            ans += int(n) ** k
        return ans == N