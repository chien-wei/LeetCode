class Solution:
    def longestLine(self, M):
        dp = [[[0 for _ in range(4)] for _ in range(len(M[0]))] for _ in range(len(M))]
        # 0: vertical, 1: horizontal, 2: diagonal, 3: anti-diagonal

        res = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    # vertical
                    dp[i][j][0] = 1
                    if i > 0:
                        dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0] + 1)

                    # horizontal
                    dp[i][j][1] = 1
                    if j > 0:
                        dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1] + 1)

                    # diagonal
                    dp[i][j][2] = 1
                    if i > 0 and j > 0:
                        dp[i][j][2] = max(dp[i][j][2], dp[i-1][j-1][2] + 1)

                    # anti-diagonal
                    dp[i][j][3] = 1
                    if i > 0 and j < len(M[0])-1:
                        dp[i][j][3] = max(dp[i][j][3], dp[i-1][j+1][3] + 1)

                res = max(res, max(dp[i][j]))
        return res

s = Solution()
print(s.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))

print(s.longestLine([[0,1,1,0,1],[0,1,1,1,1],[1,0,0,0,1]]))

print(s.longestLine([[]]))

print(s.longestLine([[0,1,1,0,1],[0,1,0,0,0],[1,0,0,0,1],[0,0,0,0,1]]))