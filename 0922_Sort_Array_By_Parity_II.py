class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(A):
            if i % 2 == 1 and A[i] % 2 == 0:
                j = i+1
                while j < len(A) and A[j] % 2 == 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
                
            elif i % 2 == 0 and A[i] % 2 == 1:
                j = i+1
                while j < len(A) and A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 1
        return A