class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. build count1 dict
        # 2. go over s2, three cases:
        #   a. if c2 not in count1, not possible, start over after that c2
        #   b. elif c2 not in count2, slide i until c2 is back to count2
        #   c. else c2 in count2, go on
        count1 = {}
        for c1 in s1:
            count1[c1] = count1.get(c1, 0) + 1
        
        N = len(s2)
        i, j = 0, 0
        count2 = dict(count1)
        while j < N:
            if s2[j] not in count1:
                count2 = dict(count1)
                j += 1
                i = j
                continue
                
            while s2[j] not in count2:
                count2[s2[i]] = count2.get(s2[i], 0) + 1
                i += 1
                
            count2[s2[j]] -= 1
            if count2[s2[j]] == 0:
                count2.pop(s2[j])
                
            # step end
            if len(count2) == 0:
                return True
            
            j += 1
        return False