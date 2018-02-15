class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        print(collections.Counter(s))
        for c, i in collections.Counter(s).most_common():
            res += c*i
        return res