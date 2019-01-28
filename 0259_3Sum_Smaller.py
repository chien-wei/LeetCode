class Solution:
    def threeSumSmaller(self, nums, t):
        if len(nums) < 3:
            return 0
        ns = sorted(nums)
        res = 0
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                if ns[l] + ns[r] + ns[i] < t:
                    res += r-l
                    l += 1
                elif ns[l] + ns[r] + ns[i] >= t:
                    r -= 1
        return res

s = Solution()
print(s.threeSumSmaller([-2, 0, 1, 3], 2))