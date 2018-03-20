class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        check = num
        count = 0
        list_a = []
        if num == 1:
            return False
        elif num == 6:
            return True
        for x in range(2, check / 4):
            #print x
            if x != 0 and check % x == 0 and x not in list_a:
                count += x
                count += check / x
                list_a.append(check/x)

                #print x, check / x, count
        if count + 1 == num:
            return True
        else: return False
        '''
        if num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336:
            return True
        return False

S = Solution()
print S. checkPerfectNumber(20666666)

