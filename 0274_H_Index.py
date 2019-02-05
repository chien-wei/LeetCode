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

# 2019/02/05 update
class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        if len(citations) == 0:
            return 0
        citations.sort()
        N = len(citations)-1
        i = 0
        for c in citations:
            #print(i, citations[N-i])
            if i+1 > citations[N-i]:
                return i
            i += 1
        if i == len(citations):
            return i
        return 0