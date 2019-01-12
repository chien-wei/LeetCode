class Solution:
    def StrobogrammaticNumber(self, num):
        strobogrammatic = {'0': '0', 
                           '1': '1',
                           '6': '9',
                           '8': '8',
                           '9': '6'}
        s = str(num)
        N = len(s)-1
        for i in range(len(s)//2 + 1):
            if strobogrammatic[s[i]] != s[N - i]:
                return False
        return True

s = Solution()
print(s.StrobogrammaticNumber('69'))
print(s.StrobogrammaticNumber('881'))
print(s.StrobogrammaticNumber('80108'))
print(s.StrobogrammaticNumber('6119'))