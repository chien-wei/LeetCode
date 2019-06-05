class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda s: s[::-1], s.split()))