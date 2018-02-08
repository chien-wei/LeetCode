class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for _str in strs:
            h = {}
            sort = ''.join(sorted(_str))
            groups[sort] = groups.get(sort, [])
            groups[sort].append(_str)
        return list(groups.values())