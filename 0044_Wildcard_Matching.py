class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # Top-down: TLE
        '''
        def match(s, p):
            if len(s) + len(p) == 0:
                return True
            if len(s) == 0 and len(set(p)) == 1 and p[0] == '*':
                return True
            elif len(s) == 0 or len(p) == 0:
                return False
            
            ans = False
            if p[0] == '?':
                ans = ans or match(s[1:], p[1:])
            elif p[0] == '*':
                for i in range(len(s)+1):
                    ans = ans or match(s[i:], p[1:])
            elif p[0] == s[0]:
                ans = ans or match(s[1:], p[1:])
            return ans
        
        return match(s, p)
        '''
        
        # 
        '''
        if len(s) + len(p) == 0:
            return True
        if len(s) == 0 and len(set(p)) == 1 and p[0] == '*':
            return True
        elif len(s) == 0 or len(p) == 0:
            return False
        
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(p)+1)]

        dp[0][0] = 1
        if p[0] == '*':
            dp[1][0] = 1
        #print(dp)
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if (p[i-1] == '?' or p[i-1] == s[j-1]) and dp[i-1][j-1] == 1:
                    dp[i][j] = 1
                elif p[i-1] == '*':
                    if dp[i-1][j] == 1 or dp[i][j-1] == 1:
                        dp[i][j] = 1
            #print(dp)
        return dp[len(p)][len(s)] == 1
        '''
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True]  + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        return dp[-1]
    
    