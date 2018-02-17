class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_times = [] # stack for times
        s_strings = [] # stack for strings
        i = 0
        num = ""
        string = ""
        isstr = False
        s = '1[' + s + ']'
        for c in s:
            if c >= "0" and c <= "9":
                if isstr:
                    s_strings.append(string)
                    string = ""
                    isstr = False
                elif not isstr and string != "":
                    s_strings[-1] += string
                    string = ""
                #print("number: " + c)
                num += c
            elif c =='[':
                s_times.append(num)
                num = ""
                isstr = True
            elif c ==']':
                if isstr:
                    s_strings.append(string)
                    string = ""
                    isstr = False
                elif not isstr and string != "":
                    s_strings[-1] += string
                    string = ""
                t, a = int(s_times.pop()), s_strings.pop()
                if s_strings:
                    s_strings[-1] += t*a
                else:
                    return t*a
            else:
                string += c
            #print(s_times, s_strings, string)

# There is also regex solution:
# def decodeString(self, s):
#     while '[' in s:
#         s = re.sub(r'(\\d+)\\[([a-z]*)\\]', lambda m: int(m.group(1)) * m.group(2), s)
#     return s
