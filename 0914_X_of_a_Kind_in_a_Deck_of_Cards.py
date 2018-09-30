from functools import reduce
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
            
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1
        
        return reduce(gcd, count.values()) > 1