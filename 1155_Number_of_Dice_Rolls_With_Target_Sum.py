class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0 for _ in range(target+1)]
        for i in range(1, f+1):
            if i < len(dp):
                dp[i] += 1
            
        for i in range(d-1):
            new_dp = [0 for _ in range(target+1)]
            for j in range(len(dp)):
                if dp[j] != 0:
                    for k in range(1, f+1):
                        if j + k < len(dp):
                            new_dp[j+k] += dp[j]
            dp = new_dp
        return dp[-1] % (10**9 + 7)