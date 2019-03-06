# union find: accepted
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def find_parent(parents, num):
            if num not in parents:
                return num+1
            if parents[num] != num:
                return parents[num]
            parents[num] = find_parent(parents, num-1)
            return parents[num]
        
        parents = {}
        for num in nums:
            parents[num] = num
        for num in nums:
            parents[num] = find_parent(parents, num-1)
        result = 0
        for p in parents:
            result = max(result, abs(p - parents[p] + 1))
        return result

# hash: accepted
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = {}
        for num in nums:
            exist[num] = 1
        result = 0
        for num in nums:
            tmp = 1
            while num+tmp in exist:
                tmp += 1
            result = max(result, tmp)
        return result