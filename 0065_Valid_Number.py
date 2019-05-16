class Solution:
    def isNumber(self, s: str) -> bool:
        NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        hasPosNeg = hasInt = hasPoint = hasIntAfterPoint = hasExp = hasExpPosNeg = hasExpInt = False 
        s = s.strip()
        for i, c in enumerate(s):
            if (c == "+" or c == "-") and i == 0:
                hasPosNeg = True
            elif c == "." and not hasPoint and not hasExp:
                hasPoint = True
            elif hasExp and not hasExpPosNeg and (c == "+" or c == "-") and not hasExpInt:
                hasExpPosNeg = True
            elif c in NUMBERS and not hasPoint and not hasExp:
                hasInt = True
            elif c in NUMBERS and hasPoint and not hasExp:
                hasIntAfterPoint = True
            elif c == "e" and not hasExp and (hasInt or (hasPoint and (hasInt or hasIntAfterPoint))):
                hasExp = True
            elif c in NUMBERS and hasExp:
                hasExpInt = True
            else:
                return False
        #print(hasInt, hasExp, hasExpInt)
        return (hasInt or (hasPoint and (hasInt or hasIntAfterPoint))) and (not hasExp or (hasExp and hasExpInt))

s = Solution()
print(s.isNumber("0") == True)
print(s.isNumber(" 0.1 ") == True)
print(s.isNumber("abc") == False)
print(s.isNumber("1 a") == False)
print()
print(s.isNumber("2e10") == True)
print(s.isNumber(" -90e3   ") == True)
print(s.isNumber(" 1e") == False)
print(s.isNumber("e3") == False)
print()
print(s.isNumber(" 6e-1") == True)
print(s.isNumber(" 99e2.5 ") == False)
print(s.isNumber("53.5e93") == True)
print(s.isNumber(" --6 ") == False)
print()
print(s.isNumber("-+3") == False)
print(s.isNumber("95a54e53") == False)
print(s.isNumber(".1") == True)
print(s.isNumber(".") == False)
print()
print(s.isNumber("3.") == True)
print(s.isNumber("3.e2") == True)
print(s.isNumber(".1e0") == True)
print(s.isNumber("0..") == False)
print()
print(s.isNumber("+.8") == True)
print(s.isNumber("459277e38+") == False)