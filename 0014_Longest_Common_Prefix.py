class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        pre = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while len(strs[i]) > j and len(pre) > j and strs[i][j] == pre[j]:
                j += 1
            pre = pre[:j]
        return pre
                