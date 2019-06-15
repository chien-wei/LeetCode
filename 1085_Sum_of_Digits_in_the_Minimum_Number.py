class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        mn = min(A)
        sm = 0
        while mn > 0:
            sm += mn % 10
            mn //= 10
        return 0 if sm & 1 == 1 else 1