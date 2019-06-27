from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # LIS plus memo last indices
        dp = defaultdict(lambda: {0:1}) # {9: {0:1}, 4: {0:1, -5: 2}, 7: {0:1, 3:2, -2:2}, ...}
        res = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[j] - A[i]
                if diff in dp[j]:
                    dp[i][diff] = max(dp[i].get(diff, 2), dp[j][diff] + 1)
                else:
                    dp[i][diff] = dp[i].get(diff, 2)
                res = max(res, dp[i][diff])
        return res