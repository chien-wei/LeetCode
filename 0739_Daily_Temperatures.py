class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 0:
            return[]
        elif len(T) == 1:
            return [0]
        stack = []
        res = []
        for i in range(len(T)-1, -1, -1):
            # print(stack, res)
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            if len(stack) == 0:
                res.insert(0, 0)
            else:
                res.insert(0, stack[-1] - i)
                
            stack.append(i)
            
        return res