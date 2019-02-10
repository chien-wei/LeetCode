class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        if len(A) == 0:
            return 0
        res = 0
        i, j = 0, 0
        cur = {}
        while j < len(A):
            if A[j] not in cur:
                cur[A[j]] = 1
            else:
                cur[A[j]] += 1
                
            while len(cur) > K:
                cur[A[i]] -= 1
                if cur[A[i]] == 0:
                    cur.pop(A[i])
                i += 1
                
            if len(cur) == K:
                tmp = i
                tmp_cur = dict(cur)
                while len(tmp_cur) == K:
                    #print(A[tmp:j+1])
                    res += 1
                    tmp_cur[A[tmp]] -= 1
                    if tmp_cur[A[tmp]] == 0:
                        tmp_cur.pop(A[tmp])
                    tmp += 1
                    #print(cur, tmp_cur)
                    
            j += 1
                        
        return res
                