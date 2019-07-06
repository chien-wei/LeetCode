class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M == 2:
            if Y % 100 == 0 and Y % 400 != 0:
                return 28
            if Y % 4 == 0:
                return 29
            else:
                return 28
        elif M in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30