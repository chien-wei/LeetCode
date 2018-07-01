class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        money = {5: 0, 10: 0, 20: 0}
        result = True
        for bill in bills:
            if bill == 5:
                money[5] += 1
            elif bill == 10 and money[5] > 0:
                money[10] += 1
                money[5] -= 1
            elif bill == 20 and ((money[5] > 0 and money[10] > 0) or money[5] > 2):
                if money[5] > 0 and money[10] > 0:
                    money[20] += 1
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] > 2:
                    money[5] -= 3
            else:
                result = False
                break
        return result