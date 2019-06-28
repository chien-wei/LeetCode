class Solution(object):
    def complexNumberMultiply(self, a, b):
        real = 0
        i = 0
        a1, a2 = a.split('+')
        a2 = int(a2.split('i')[0])
        a1 = int(a1)
        b1, b2 = b.split('+')
        b1 = int(b1)
        b2 = int(b2.split('i')[0])

        real = a1 * b1 - a2 * b2
        i = a1 * b2 + a2 * b1
        return str(real) + '+' + str(i) + 'i'

S = Solution()
S.complexNumberMultiply("1+-1i", "1+-1i")
