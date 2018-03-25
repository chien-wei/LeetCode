class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count = 0
        line = 1
        for s in S:
            c = ord(s) - ord('a')
            if count + widths[c] <= 100:
                count += widths[c]
            else:
                line += 1
                count = widths[c]
            print(count, line)
        return [line, count]