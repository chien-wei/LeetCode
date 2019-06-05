from typing import List
from collections import defaultdict

class Solution:
    def WordDistance(self, words: List[str]):
        self.dic = defaultdict(list)
        for i, word in enumerate(words):
            self.dic[word].append(i)

    
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.dic[word1], self.dic[word2]
        res = float('inf')
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res


s = Solution()
s.WordDistance(["practice", "makes", "perfect", "coding", "makes"])
assert s.shortest("coding", "practice") == 3
assert s.shortest("coding", "makes") == 1