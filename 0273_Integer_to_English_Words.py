class Solution:
    def numberToWords(self, num: int) -> str:
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        if num == 0:
            return "Zero"
        snum = str(num)
        thousand = 0
        res = []
        
        for i in range(len(snum), 0, -3):
            tmp = []
            hundreds = snum[max(0, i-3):i]
            while len(hundreds) < 3:
                hundreds = "0" + hundreds
            if int(hundreds[0]) > 0:
                tmp.append(LESS_THAN_20[int(hundreds[0])])
                tmp.append("Hundred")
            if int(hundreds[1:]) > 19:
                tmp.append(TENS[int(hundreds[1])])
                tmp.append(LESS_THAN_20[int(hundreds[2])])
            else:
                tmp.append(LESS_THAN_20[int(hundreds[1:])])

            res = tmp + [THOUSANDS[thousand]] + res if int(hundreds) > 0 else tmp + res
            thousand += 1
        return " ".join(filter(lambda x: x != "", res))