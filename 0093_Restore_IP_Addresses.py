class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # e.g. 25525511135
        # 2 =>
        # 25 =>
        # 255 => 
        # if reach the end, store the result
        # classic backtracking
        # be careful about 0: not at first element for number > 0
        # and not repeat if the value is 0
        
        def backtrack(s, i, acc, res):
            #print(i, acc, res)
            if len(acc) == 4 and i == len(s):
                res.append('.'.join(acc))
                return
            elif len(acc) > 4:
                return
            elif i >= len(s):
                return
            
            for j in range(i + 1, i + 4):
                if int(s[i:j]) < 256 and len(str(int(s[i:j]))) == j-i:
                    acc.append(s[i:j])
                    backtrack(s, j, acc[:], res)
                    acc.pop()
        
        res = []
        backtrack(s, 0, [], res)
        return res