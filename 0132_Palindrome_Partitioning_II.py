# refer: https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space

class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        cut = [i-1 for i in range(N+1)]
        
        for i in range(N):
            # odd palindrome
            for j in range(N):
                if i - j >= 0 and i + j < N and s[i-j] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1], 1 + cut[i-j])
                else:
                    break
            
            # even palindrome
            for j in range(1, N):
                if i - j + 1 >= 0 and i + j < N and s[i-j+1] == s[i+j]:
                    cut[i+j+1] = min(cut[i+j+1], 1 + cut[i-j+1])
                else:
                    break
        return cut[N]
        