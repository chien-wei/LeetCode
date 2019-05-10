class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            result = str(chr((n-1) % 26 + ord("A"))) + result
            n = (n-1) // 26
        return result