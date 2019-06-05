from typing import List

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        last = -float('inf')
        res = float('inf')
        for i, word in enumerate(words):
            if word == word1 or word == word2:
                if last >= 0 and (word1 == word2 or words[last] != word):
                    res = min(res, i - last)
                last = i
        
        return res

s = Solution()
assert s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes") == 3
assert s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes") == 1