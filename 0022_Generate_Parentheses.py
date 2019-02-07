class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
    
        cand = { "(": n, ")": 0 }
        res = []
          
        def helper(acc, cand, res):
            if cand["("] + cand[")"] == 0:
                res.append(acc)
            if cand["("] > 0:
                cand["("] -= 1
                cand[")"] += 1
                helper(acc+"(", cand, res)
                cand["("] += 1
                cand[")"] -= 1
            if cand[")"]:
                cand[")"] -= 1
                helper(acc+")", cand, res)
                cand[")"] += 1
            
        helper("", cand, res)
        return res