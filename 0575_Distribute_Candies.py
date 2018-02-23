class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = collections.Counter(candies)
        return len(count) if len(count) <= len(candies)/2 else int(len(candies)/2)