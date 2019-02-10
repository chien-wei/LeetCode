class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        
        def helper(y, acc):
            if y == X:
                return acc
            elif y < X:
                return acc + X - y
            else:
                if y % 2 == 1:
                    return helper((y+1)//2, acc+2)
                else:
                    return helper(y//2, acc+1)
            
        return helper(Y, 0)