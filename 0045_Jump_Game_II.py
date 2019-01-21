# This solution get TLE
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        N = len(nums)
        mn = [float('inf') for _ in range(N)]
        mn[0] = 0
        for i in range(1, N):
            for j in range(i, i+nums[i-1]):
                if j < len(mn):
                    mn[j] = min(mn[j], mn[i-1]+1)
                else:
                    break
        return mn[N-1] if mn[N-1] != float('inf') else 0

# accepted with little optimization
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        N = len(nums)
        mn = [float('inf') for _ in range(N)]
        mn[0] = 0
        cur = 1
        for i in range(1, N):
            for j in range(cur, i+nums[i-1]):
                if j < len(mn):
                    mn[j] = min(mn[j], mn[i-1]+1)
                else:
                    break
            cur = max(cur, i+nums[i-1])
        return mn[N-1] if mn[N-1] != float('inf') else 0
