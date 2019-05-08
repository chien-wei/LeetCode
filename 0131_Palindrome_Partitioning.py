class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        def backtrack(s, i, acc, res):
            if i == len(s):
                res.append(acc)
            for k in range(i+1, len(s)+1):
                if isPalindrome(s[i:k]):
                    acc.append(s[i:k])
                    backtrack(s, k, acc[:], res)
                    acc.pop()
                    
        res = []
        backtrack(s, 0, [], res)
        return res