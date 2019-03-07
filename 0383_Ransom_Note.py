class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = {}
        need = {}
        
        for m in magazine:
            have[m] = have.get(m, 0) + 1
        for r in ransomNote:
            need[r] = need.get(r, 0) + 1
        
        for n in need:
            if have.get(n, 0) < need[n]:
                return False
        return True