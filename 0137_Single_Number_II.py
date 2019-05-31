class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # need a cycle in three => need 2 bits
        # try to make 00 => 01 => 10 => 00
        n1 = n2 = 0
        for num in nums:
            n1 = (n1 ^ num) & ~n2
            n2 = (n2 ^ num) & ~n1
        return n1