class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        if len(A) == 0 and K == 0:
            return [0]
        carry = 0
        i = len(A)-1
        res = []
        quotient = K
        while i >= 0:
            remain = quotient % 10
            quotient = quotient // 10
            res.insert(0, (carry + remain + A[i]) % 10)
            carry = (carry + remain + A[i]) // 10
            i -= 1
        while quotient > 0:
            remain = quotient % 10
            quotient = quotient // 10
            res.insert(0, (carry + remain) % 10)
            carry = (carry + remain) // 10
        
        if carry > 0:
            res.insert(0, carry)
        return res