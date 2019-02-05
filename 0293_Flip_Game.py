class Solution:
    def generatePossibleNextMoves(self, s: 'str'):
        res = []
        for i in range(1, len(s)):
            if s[i-1: i+1] == '++':
                res.append(s[:i-1] + '--' + s[i+1:])
        return res

s = Solution()
print(s.generatePossibleNextMoves("++++"))
print(s.generatePossibleNextMoves("----"))
print(s.generatePossibleNextMoves(""))