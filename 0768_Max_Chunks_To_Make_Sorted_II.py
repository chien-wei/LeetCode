class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_ = 0
        result = 0
        max_count = 0
        sort = sorted(arr[:])
        for i, n in enumerate(arr):
            if n > max_:
                max_ = n
                max_count = 1
            elif n == max_:
                max_count += 1
                    
            if sort[i] == max_ and max_count == 1:
                result += 1
                max_count = 0
            elif sort[i] == max_:
                max_count -= 1
                
        return result


# One other solution provide by lee215, using collections.Counter() is pretty cool.
#   def maxChunksToSorted(self, arr):
#       res, c1, c2 = 0, collections.Counter(), collections.Counter()
#       for a, b in zip(arr, sorted(arr)):
#           c1[a] += 1
#           c2[b] += 1
#           res += c1 == c2
#       return res