class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        N = max(len(arr1), len(arr2))
        
        ra1 = arr1[::-1] + [0] * (N - len(arr1))
        ra2 = arr2[::-1] + [0] * (N - len(arr2))
        res = []
        print(ra1, ra2)
        carry = 0
        
        for i in range(N):
            d = ra1[i] + ra2[i] + carry
            if d < 0:
                res.append(1)
                carry = 1
            else:
                res.append(d % 2)
                carry = -(d // 2)
        if carry == -1:
            res.append(1)
            res.append(1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return res[::-1]