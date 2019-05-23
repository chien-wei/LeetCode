class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 0 => 0
        # 1 => [0, 1] => 2
        # 2 => [0, 1] + [11, 10] (11, 10 = (0, 1).reverse + 2)
        # 3 => [00, 01, 11, 10, 110, 111, 101, 100] =>
        # (00, 01, 11, 10).reverse + 4
        
        rate = 1
        res = [0]
        for i in range(n):
            res = res + list(map(lambda x: x + rate, res[::-1]))
            rate = rate << 1
        return res