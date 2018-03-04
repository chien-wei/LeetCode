"""
:type nums: List[int]
:rtype: List[List[int]]
"""


# DFS recursively 
class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
        
# Bit Manipulation    
class Solution:
    def subsets2(self, nums):
            res = []
            nums.sort()
            print(1<<len(nums))
            for i in range(1<<len(nums)):
                tmp = []
                for j in range(len(nums)):
                    if i & (1 << j):
                        tmp.append(nums[j])
                res.append(tmp)
            return res
    
# Iteratively
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res