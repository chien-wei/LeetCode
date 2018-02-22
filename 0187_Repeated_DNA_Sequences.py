class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        ans = set()
        seen = {}
        for i in range(0, len(s) - 9):
            cur = s[i:i+10]
            if cur in seen:
                ans.add(cur)
            else:
                seen[cur] = 1
        return list(ans)