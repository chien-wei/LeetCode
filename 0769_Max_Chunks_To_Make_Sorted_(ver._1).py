class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        p = -1
        for i, n in enumerate(arr):
            if i < p:
                p = max(p, n+1)
            elif (i == n): result += 1
            else:
                p = i
                next = n
                while next != i:
                    p = max(p, next+1)
                    next = arr[next]
                result += 1
                
            
        return result
