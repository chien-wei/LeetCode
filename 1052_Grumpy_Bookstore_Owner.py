class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        # already satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
        
        # additional satisfied by sliding window
        mx_add = 0
        add = 0
        for i in range(len(customers)):
            if i < X and grumpy[i] == 1:
                add += customers[i]
            elif i >= X:
                if grumpy[i] == 1:
                    add += customers[i]
                if grumpy[i-X] == 1:
                    add -= customers[i-X]
            mx_add = max(mx_add, add)
            
        return res + mx_add