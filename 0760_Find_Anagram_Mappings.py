class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        P = []
        for a in A:
            i = 0
            for b in B:
                if(b == a):
                    P.append(i)
                    break
                i = i + 1
        return P