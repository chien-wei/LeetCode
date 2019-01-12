class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        ind_plus = len(digits)-1
        while ind_plus >= 0 and digits[ind_plus] == 9:
            digits[ind_plus] = 0
            ind_plus -= 1
            
        if ind_plus == -1:
            return [1] + digits
        digits[ind_plus] += 1
        
        return digits