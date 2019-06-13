from collections import defaultdict
from typing import List
class Solution:
    def alienOrder(self, words: List[str]):
        NUM_ALPHABET = 26

        def dfs(dp, idx, visited, res):
            print(idx, visited, res)
            if not dp[idx][idx]:
                return True

            visited[idx] = True
            for i in range(NUM_ALPHABET):
                if i == idx or not dp[idx][i]:
                    continue
                if visited[i]:
                    return False
                if not dfs(dp, i, visited, res):
                    return False
            
            visited[idx] = False
            dp[idx][idx] = False
            res.append(chr(ord('a') + idx))
            return True

        dp = [[False for _ in range(NUM_ALPHABET)] for _ in range(NUM_ALPHABET)]
        visited = defaultdict(lambda: False)
        # to pass string, pass char list is easier
        res = []
        # first set every occuried alphabet in dp True
        for word in words:
            for c in word:
                i = ord(c) - ord('a')
                dp[i][i] = True
        # if we are sure that b > a, dp[1][0] = True
        for i in range(1, len(words)):
            j = 0
            while words[i][j] == words[i-1][j]:
                j += 1
            c1, c2 = ord(words[i][j]) - ord('a'),  ord(words[i-1][j]) - ord('a')
            # if we are sure that b > a, but get a > b later. This is invalid, so return ""
            if dp[c2][c1]:
                return ""
            dp[c1][c2] = True

        # for each alphabet, use dfs to find which has longer order list
        for i in range(NUM_ALPHABET):
            if not dfs(dp, i, [False for _ in range(NUM_ALPHABET)], res):
                return ""   
        return "".join(res)

s = Solution()
assert s.alienOrder(["aa","ab","bb","bc"]) == "abc"
assert s.alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf"
assert s.alienOrder(["z","x"]) == "zx"
assert s.alienOrder(["z","x","z"]) == ""
assert s.alienOrder(["wrt","wt","er"]) == "wert"
