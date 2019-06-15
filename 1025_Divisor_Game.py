class Solution:
    def divisorGame(self, N: int) -> bool:
        # try some example from 2 ~ 10 and found it just ask odd and even
        return N & 1 == 0 