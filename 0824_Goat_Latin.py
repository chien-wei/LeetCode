class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S == "":
            return ""
        result = ""
        a_count = 0
        for s in S.split(" "):
            a_count += 1
            tmp = ""
            need_ma = 0
            for i in range(len(s)):
                if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                    result += s[i]
                    if i == 0:
                        need_ma = 1
                else:
                    if i == 0:
                        tmp += s[i]
                        need_ma = 1
                    else:
                        result += s[i]
            result += tmp
            if need_ma == 1:
                result += "ma"
            for j in range(a_count):
                result += 'a'
            if a_count != len(S.split(" ")):
                result += " "
        return result