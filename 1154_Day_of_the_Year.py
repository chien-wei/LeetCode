class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        res = 0
        month -= 1
        while month > 0:
            if month == 2:
                if year % 100 == 0 and year % 400 != 0:
                    res += 28
                elif year % 4 == 0:
                    res += 29
                else:
                    res += 28
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                res += 31
            else:
                res += 30
            month -= 1
        return res + day