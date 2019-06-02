class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        
        def gcdString(s1, s2):
            if len(s1) >= len(s2) and not s1.startswith(s2):
                return ""
            if s2 == "":
                return s1
            return gcdString(s2, s1[len(s2):] if s1.startswith(s2) else s1)
        
        return gcdString(str1, str2)