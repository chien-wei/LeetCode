class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {'0':0, '1':1, '8':8, '2':5, '5':2, '6':9, '9':6}
        count = 0
        
        for i in range(1, N+1):
            mark = False
            for c in str(i):
                if c not in d:
                    mark = False
                    break
                elif c == '0' or c == '1' or c == '8':
                    continue
                else:
                    mark = True
            if mark:
                count += 1
        return count