class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        chars = {}
        i = j = 0
        while j < K:
            if S[j] not in chars:
                chars[S[j]] = 0
            chars[S[j]] += 1
            j += 1
        
        res = 0
        while j < len(S):
            if len(chars.keys()) == K:
                res += 1
            chars[S[i]] -= 1
            if chars[S[i]] == 0:
                chars.pop(S[i])
            i += 1
                
            if S[j] not in chars:
                chars[S[j]] = 0
            chars[S[j]] += 1
            j += 1
            
        if len(chars.keys()) == K:
            res += 1
            
        return res