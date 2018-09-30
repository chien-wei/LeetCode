class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left_max = [a for a in A]
        right_min = [a for a in A]
        for i in range(1, len(A)):
            left_max[i] = max(left_max[i-1], left_max[i])
        
        for i in range(len(A)-2, -1, -1):
            right_min[i] = min(right_min[i], right_min[i+1])
        
        for i in range(len(A)-1):
            if left_max[i] <= right_min[i+1] and right_min[i] <= left_max[i+1]:
                return i+1
        return len(A)