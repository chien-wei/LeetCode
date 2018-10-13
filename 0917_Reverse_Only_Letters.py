class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp = ''
        for s in S:
            if (s >= 'a' and s <= 'z') or (s >= 'A' and s <='Z'):
                tmp += s
        tmp = tmp[::-1]
        res = ''
        for s in S:
            if (s >= 'a' and s <= 'z') or (s >= 'A' and s <='Z'):
                res += tmp[0]
                tmp = tmp[1:]
            else:
                res += s
        return res