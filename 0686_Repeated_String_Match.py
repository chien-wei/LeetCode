class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 0 or len(B) == 0:
            return 0
        mx_time = len(B) // len(A)
        
        # There is case like A = 'abcd', B = 'da', so we should always check from 1
        # plus head, tail, so +2, +3 is bound
        for i in range(1, mx_time+3):
            if B in A * i:
                return i
        
        return -1
            