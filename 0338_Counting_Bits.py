class Solution:
    def countBits(self, num: int) -> List[int]:
        # even numbers => 2, 4, 6, 8 => [10, 100, 110, 1000]
        # if n in countBits(n) is even, it is same as countBits(n / 2)
        # odd numbers => 3, 5, 7 => [11, 101, 111]
        # if n in countBits(n) is odd, it is same as countBits(n - 1) + 1
        
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i // 2]
            
        return res