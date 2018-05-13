class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            new_s = ''
            cur_char = s[0]
            num = 1
            for j in range(1, len(s)):
                if s[j] == cur_char:
                    num += 1
                else:
                    new_s += str(num) + cur_char
                    cur_char = s[j]
                    num = 1
            new_s += str(num) + cur_char
            s = new_s
            
        return s