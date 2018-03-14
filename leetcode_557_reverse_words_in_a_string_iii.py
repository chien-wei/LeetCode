class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for w in s.split(' '):
            ans += w[::-1]
            ans += ' '
        return ans[0:len(ans)-1]
S = Solution()
print(S.reverseWords("Let's take LeetCode contest"))
