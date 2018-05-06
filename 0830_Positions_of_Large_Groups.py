class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        cur_len = 0
        start = end = 0
        i = 0
        pre = ""
        result = []
        for s in S:
            if cur_len == 0:
                cur_len += 1
                start = i
                end = i
            elif pre != s:
                if cur_len > 2:
                    result.append([start, end])
                cur_len = 1
                start = i
                end = i
            elif pre == s:
                cur_len += 1
                end = i
            pre = s
            i += 1
        if cur_len > 2:
            result.append([start, end])
        return result