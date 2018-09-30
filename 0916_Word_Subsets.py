class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        class our_dict(dict):
            def __contains__(self, other):
                for b in other:
                    if other[b] > self.get(b, 0):
                        return False
                return True
            def __or__(self, other):
                res = self
                for b in other:
                    if other[b] > res.get(b, 0):
                        res[b] = other[b]
                return res
                
        dB = our_dict({})
        for b in B:
            tmp = our_dict({})
            for c in b:
                tmp[c] = tmp.get(c, 0) + 1
            dB = dB | tmp
        
        res = []
        for a in A:
            tmp = our_dict({})
            for c in a:
                tmp[c] = tmp.get(c, 0) + 1
            if dB in tmp:
                res.append(a)
                
        return res