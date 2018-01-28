class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
                    
        return True