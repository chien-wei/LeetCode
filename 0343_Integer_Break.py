class Solution:
    def integerBreak(self, n: int) -> int:
        # 6 => 3 + 3, 3 * 3 = 9
        # 7 => 3 + 4, 3 * 4 = 12
        # 8 => 3 + 3 + 2 = 18
        # 9 => 3 + 3 + 3 = 27
        # 10 => 3 + 3 + 4 = 36
        # 11 => 3 + 3 + 3 + 2 = 54
        
        # k * 3 => 3 + ... = 3 ** k
        # k * 3 + 1 => 4 + 3 + .. = 4 * 3 ** k-1 = 3 ** k + 3 ** k-1
        # k * 3 + 2 => 2 * 3 ** k
        mx = [0, 1, 1, 2, 4, 6, 9, 12]
        if n > 7:
            mx = mx + [0] * (n - 7)
        
        for i in range(8, n + 1):
            if i % 3 == 0:
                mx[i] = mx[i - 3] * 3
            elif i % 3 == 1:
                mx[i] = mx[i - 4] * 4
            elif i % 3 == 2:
                mx[i] = mx[i - 2] * 2
            print(mx)
        return mx[n]