class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # becuse the number in the array is distinct and range from [0, arr.length-1]
        # if the current _max from number n is found at index i, that mean we can build a chuck
        result = 0
        max_ = 0
        for i, n in enumerate(arr):
            if n >= max_:
                max_ = n
            if i == max_:
                result += 1
        return result
