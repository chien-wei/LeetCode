class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "D", "C", "L", "X", "V", "I"][::-1]
        #values = [1000, 500, 100, 50, 10, 5, 1][::-1]
        
        result = ""
        key = 0
        while num > 0:
            digit = num % 10
            
            if digit < 4:
                result = symbols[key] * digit + result
            elif digit == 4 and key+1 < len(symbols):
                result = symbols[key] + symbols[key+1] + result
            elif digit == 5 and key+1 < len(symbols):
                result = symbols[key+1] + result
            elif digit == 9 and key+2 < len(symbols):
                result = symbols[key] + symbols[key+2] + result
            elif key+1 < len(symbols):
                result = symbols[key+1] + symbols[key] * (digit-5) + result
                
            num = num // 10
            key += 2
            
        return result