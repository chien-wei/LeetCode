class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # find LCS of str1, str2
        # build the result
        
        def LCS(str1, str2):
            M, N = len(str1), len(str2)
            dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
            for i in range(M+1):
                for j in range(N+1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1 if str1[i-1] == str2[j-1] else max(dp[i-1][j], dp[i][j-1])
            # traceback to get string
            i, j = M, N
            ans = ""
            while dp[i][j] != 0:
                while dp[i][j] == dp[i][j-1]:
                    j -= 1
                while dp[i][j] == dp[i-1][j]:
                    i -= 1
                ans = str1[i-1] + ans
                i -= 1
                j -= 1
            return ans
        
        lcs = LCS(str1, str2)
        # build result
        res = ""
        i, j, k = 0, 0, 0
        while k < len(lcs):
            while i < len(str1) and str1[i] != lcs[k]:
                res = res + str1[i]
                i += 1
            while j < len(str2) and str2[j] != lcs[k]:
                res = res + str2[j]
                j += 1
            res = res + lcs[k]
            i, j, k = i+1, j+1, k+1
        return res + str1[i:] + str2[j:]