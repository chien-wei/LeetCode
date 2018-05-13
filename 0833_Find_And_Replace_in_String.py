class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        ans = ""
        pass2 = 0
        for i in range(len(S)):
            if i < pass2:
                continue
            if i in indexes:
                j = indexes.index(i)
                #print(j)
                l = len(sources[j])
                #print(sources[j], S[i:i+l])
                if sources[j] == S[i:i+l]:
                    ans += targets[j]
                    pass2 = i+l
                else:
                    ans += S[i]
                    
            else:
                ans += S[i]
        return ans