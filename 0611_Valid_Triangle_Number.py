class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # A[i] + A[j] > A[k]
        nums.sort()
        N = len(nums)
        res = 0
        for k in range(N-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
            
        return res