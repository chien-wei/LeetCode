# https://leetcode.com/problems/digit-count-in-range/discuss/303469/Amazing-O(logN)-python-7-lines

# Same as question 233. Number of Digit One
# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         pivot, res = 1, 0
#         while n >= pivot:
#             res += n // (10 * pivot) * pivot + min(pivot, max(n % (10 * pivot) - pivot + 1, 0))
#             pivot *= 10
#         return res
# We should care when d == 0 in this question.

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def helper(n, k):
            pivot, res = 1, 0
            while n >= pivot:
                res += (n // (10 * pivot)) * pivot + min(pivot, max(n % (10 * pivot) - k * pivot + 1, 0))
                res -= pivot if k == 0 else 0 # no leading zero
                pivot *= 10
            return res + 1 # last-digit can be zero
        return helper(high, d) - helper(low-1, d)