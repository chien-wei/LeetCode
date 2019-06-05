from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = p2 = -float('inf')
        res = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                res = min(res, i - p2)
                p1 = i
            elif word == word2:
                res = min(res, i - p1)
                p2 = i
        return res

s = Solution()
assert s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") == 3
assert s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes") == 1