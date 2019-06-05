# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
# This link shows the relationship of index, which is easier to implement.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        M, N = len(num1), len(num2)
        res = [0 for _ in range(M + N)]
        for i in range(M):
            for j in range(N):
                res[i+j+1] += int(num1[i]) * int(num2[j])
        
        for k in range(len(res)-1, -1, -1):
            if k-1 >= 0:
                res[k-1] += res[k] // 10
            res[k] = str(res[k] % 10)
            
        while len(res) > 1 and res[0] == "0":
            res = res[1:]
        return "".join(res)