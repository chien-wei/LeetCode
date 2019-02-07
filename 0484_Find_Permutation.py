class Solution:
    def findPermutation(self, s):
        i, j = 0, 0
        res = ""
        for k in range(len(s)+1):
            res += str(k+1)
        
        while i < len(res):
            j = i
            while j < len(res)-1 and s[j] == "D":
                j += 1
            
            if j > i:
                res = res[:i] + res[i:j+1][::-1] + res[j+1:]
            i = j


            i += 1
            
        return res

s = Solution()
print(s.findPermutation("IDDI"))
print(s.findPermutation("IIDID"))
print(s.findPermutation("DIDDI"))
print(s.findPermutation(""))
print(s.findPermutation("DDD"))