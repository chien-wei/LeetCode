class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1
        if s[-1] == '0':
            dp[-2] = 0
        else:
            dp[-2] = 1
        
        for i in range(len(s)-1)[::-1]:
            # the testcase has '00'
            if s[i] == '0':
                continue
            if int(s[i:i+2]) < 27:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
                
        return dp[0]