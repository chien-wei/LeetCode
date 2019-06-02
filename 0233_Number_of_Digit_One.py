# #of 1     list                                               range
# 1         1                                                  [1, 9]
# 11        10  11  12  13  14  15  16  17  18  19             [10, 19]
# 1         21                                                 [20, 29]
# 1         31                                                 [30, 39]
# 1         41                                                 [40, 49]
# 1         51                                                 [50, 59]
# 1         61                                                 [60, 69]
# 1         71                                                 [70, 79]
# 1         81                                                 [80, 89]
# 1         91                                                 [90, 99]
# 11        100  101  102  103  104  105  106  107  108  109   [100, 109]
# 21        110  111  112  113  114  115  116  117  118  119   [110, 119]
# 11        120  121  122  123  124  125  126  127  128  129   [120, 129]
# Try to find rule here.

# https://leetcode.com/problems/number-of-digit-one/discuss/64426/Easy-to-understand-C%2B%2B-0ms-solution-with-detailed-explanation
# So now when we look at a number n (e.g. 2356), we look at the most significant digit(2), its divisor with highest 10's power (1000), and its remainder (356), try to reduce to a smaller number iteratively.
# (1) Since most significant digit is 2, so we know range [0, 999], [1000, 1999] are included, so we add 2 * f(999).
# (2) Also, since we have [1000, 1999] covered, we should add extra 1000.
# (3) Then we look at range [2000, 2356], try to reduce it to [0, 356] by dropping most significant digit 2, it doesn't impact the final result since most significant digit is 2 not 1.
# (4) Finally, we add f(356)
# So eventually, we have
# f(2356) += (2356 / 1000) * f(1000 - 1) = 2 * f(999);
# f(2356) += (2356 / 1000 > 1 ? 1000 : 0); 
# f(2356) += (2356 / 1000 == 1 ? 356 + 1 : 0);
# f(2356) += f(356);

import math
class Solution:
    def countDigitOne(self, n: int) -> int:
        
        def count(n: int, memo: dict) -> int:
            if n <= 0:
                return 0
            if n in memo:
                return memo[n]
            # count digits
                # convert the number to scientific natation
                # sci = "{:.2e}".format(n)
                # level = 10 ** int(sci[sci.index('+')+1:])
            level = 10 ** math.floor(math.log(n, 10))

            # fix math.log(1000, 10) = 2.99999
            if level * 10 == n:
                level = n
            
            if level == 1:
                if n >= 1:
                    return 1
                else:
                    return 0

            res = 0
            res += (n // level) * count(level - 1, memo)
            res += level if n // level > 1 else 0
            res += n % level + 1 if n // level == 1 else 0
            res += count(n % level, memo)

            memo[n] = res
            print(memo)
            return res
        
        return count(n, {})


# more readable
import math
class Solution:
    def countDigitOne(self, n: int) -> int:
        def count(n: int, memo: dict) -> int:
            if n in memo:
                return memo[n]
            
            # count digits
            tmp = n
            digits = 0
            while (tmp // 10):
                digits += 1
                tmp //= 10
            level = 10 ** digits
            
            # base case
            if level == 1:
                if n >= 1:
                    return 1
                else:
                    return 0

            res = 0
            res += (n // level) * count(level - 1, memo)
            res += level if n // level > 1 else 0
            res += n % level + 1 if n // level == 1 else 0
            res += count(n % level, memo)

            memo[n] = res
            return res
        
        if n <= 0:
            return 0
        return count(n, {})