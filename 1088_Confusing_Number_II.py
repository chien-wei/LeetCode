# dfs: got TLE
class Solution:
    def confusingNumberII(self, N: int) -> int:
        b = [0, 1, 2, 3, 4, 5, 9, 7, 8, 6]
        a = [0, 1, 6, 8, 9]
        def check(x):
            t = 0
            cur = x
            while x > 0:
                t = t * 10 + b[x % 10]
                x //= 10
            return cur != t
        
        def dfs(pos, x, res):
            print(pos, x)
            if x > 0 and check(x):
                res[0] += 1
            start = 1 if pos == 0 and x == 0 else 0
            for i in range(start, 5):
                if x * 10 + a[i] <= N:
                    dfs(pos + 1, x * 10 + a[i], res)
            
        res = [0]
        dfs(0, 0, res)
        return res[0]

# TLE
class Solution:
    def confusingNumberII(self, N: int) -> int:
        
        res = [0]
        n = N
        
        def helper(cur, res):
            if (cur) > n:
                return 
            if confusingNum(cur):
                res[0] += 1
            helper(cur * 10 + 1, res)
            helper(cur * 10 + 6, res)
            helper(cur * 10 + 8, res)
            helper(cur * 10 + 9, res)
            if (cur):
                helper(cur * 10, res)
                
        def confusingNum(n):
            sum = 0
            t = n
            while n > 0:
                k = n % 10
                if k == 6:
                    k = 9
                elif k == 9:
                    k = 6
                sum = sum * 10 + k
                n //= 10
            return sum != t
        
        helper(0, res)
        return res[0]