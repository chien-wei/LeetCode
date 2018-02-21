class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        def ref(s, i):
            if i == len(s):
                ans.append(s)
                return
            elif not(s[i] >= '0' and s[i] <= '9'):
                ref(s[:i] + s[i].upper() + s[i+1:], i+1)
                ref(s[:i] + s[i].lower() + s[i+1:], i+1)
            else:
                ref(s, i+1)
        ref(S, 0)
        return ans