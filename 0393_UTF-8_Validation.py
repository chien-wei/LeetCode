class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        utf8 = False
        count = 0
        for d in data:
            if d >= 255:
                return False
            bi = "{:08b}".format(d)
            ind = bi.index('0')
            if ind == 0 and not utf8:
                continue
            elif ind > 4:
                return False
            elif utf8 and ind == 1:
                count -= 1
                if count == 0:
                    utf8 = False
            elif utf8 and ind != 1:
                return False
            elif not utf8:
                utf8 = True
                count = ind - 1
            else:
                return False
                
            #print(ind, bi, utf8, count)
        if utf8:
            return False
        return True