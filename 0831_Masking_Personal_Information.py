class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = ""
        if "@" in S:
            n = S.replace("@",".").split(".")
            result += n[0][0].lower() + "*" * 5 + n[0][-1].lower() + "@"
            result += n[1].lower() + "." + n[2].lower()
        else:
            n = S.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
            print(n)
            count = len(n)
            if count > 10:
                result += '+'
                while count > 10:
                    result += '*'
                    n = n[1:]
                    count -= 1
                result += '-'
            for i in range(3):
                result += '*'
                n = n[1:]
            result += '-'
            for i in range(3):
                result += '*'
                n = n[1:]
            result += '-'
            result += n
                
        
        return result