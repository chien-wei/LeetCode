class Solution:
    def reachNumber(self, target: int) -> int:
        # math
        if target < 0:
            target = -target
            
        cur = 0
        step = 0
        while cur < target:
            step += 1
            cur += step
        
        if cur == target:
            return step
        
        while (cur - target) & 1 == 1:
            step += 1
            cur += step
            
        return step