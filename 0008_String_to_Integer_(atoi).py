import re
class Solution:
    def myAtoi(self, string: str) -> int:
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        res = re.search('^(([+|-]\d+)|\d+)',string.strip())
        if res:
            res = res.group()
            res_int = int(res)
        else:
            res_int = 0
        res_int = min(res_int, INT_MAX)
        res_int = max(res_int, INT_MIN)
        return res_int

s = Solution()
assert s.myAtoi("42") == 42
assert s.myAtoi("   -42") == -42
assert s.myAtoi("4193 with words") == 4193
assert s.myAtoi("words and 987") == 0
assert s.myAtoi("-91283472332") == -2147483648