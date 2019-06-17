class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        M, N = len(s), len(p)
        i, j = 0, 0
        res = []
        countP = {}
        for pi in p:
            countP[pi] = countP.get(pi, 0) + 1
        
        countS = dict(countP)
        while j < M:
            #print(i, j, countS)
            if j - i + 1 > N:
                countS[s[i]] = countS.get(s[i], 0) + 1
                i += 1
            if s[j] not in countP: # has letter not in p
                countS = dict(countP)
                i = j+1
            elif s[j] not in countS: # has letter in p but used
                while s[j] not in countS:
                    countS[s[i]] = countS.get(s[i], 0) + 1
                    i += 1
                countS[s[j]] -= 1
                if countS[s[j]] == 0:
                    countS.pop(s[j])
            else: # has letter in p
                countS[s[j]] -= 1
                if countS[s[j]] == 0:
                    countS.pop(s[j])
                    
            if len(countS) == 0:
                res.append(i)
            j += 1
        return res