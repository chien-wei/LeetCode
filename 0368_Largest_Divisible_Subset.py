class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # after sorting, this quesiton is same as LIS
        nums.sort()
        N = len(nums)
        if N == 0:
            return []
        
        mxIdx = 0
        count = [1 for _ in range(N)]
        pre = [[nums[i]] for i in range(N)]
        
        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if count[i] < count[j] + 1:
                        count[i] = count[j] + 1
                        pre[i] = pre[j] + [nums[i]]
                    if count[i] > count[mxIdx]:
                        mxIdx = i
        
        return pre[mxIdx]