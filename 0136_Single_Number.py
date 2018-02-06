class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = d[num]+1 if num in d else 1
        return list(d.keys())[list(d.values()).index(1)]