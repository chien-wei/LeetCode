class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        import operator
        
        hashStart = {}
        hashEnd = {}
        for i in range(len(S)):
            if S[i] not in hashStart:
                hashStart[S[i]] = i
                hashEnd[S[i]] = [hashStart[S[i]], i]
            else:
                hashEnd[S[i]] = [hashStart[S[i]], i]
        sort = sorted(hashEnd.values())
        if len(sort) == 0:
            return []
        elif len(sort) == 1:
            return [sort[0][1] - sort[0][0] + 1]
        result = []
        start = end = -1
        for tup in sort:
            if start < 0:
                start = tup[0]
                end = tup[1]
            elif tup[0] < end:
                end = max(end, tup[1])
            elif tup[0] > end:
                result.append(end - start + 1)
                start = tup[0]
                end = tup[1]
        result.append(end - start + 1)
        return result