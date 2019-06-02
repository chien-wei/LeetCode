class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # use brute force because the limitation is not strong
        # think how to optimize it
        words = set(words)
        N = len(text)
        res = []
        for i in range(N):
            for j in range(i+1, N+1):
                if text[i:j] in words:
                    res.append([i, j-1])
        return res