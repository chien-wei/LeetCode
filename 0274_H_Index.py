class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        l = [0] * (N+1)
        for i in citations:
            if i > N:
                l[N] += 1
            else:
                l[i] += 
        
        for i in range(N, -1, -1):
            if i < N:
                l[i] += l[i+1]
            if l[i] >= i:
                return i
        return 0