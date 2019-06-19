class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        inc = [1 for _ in range(N)]
        dec = [1 for _ in range(N)]
        
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], dec[j] + 1)
                elif nums[j] > nums[i]:
                    dec[i] = max(dec[i], inc[j] + 1)
        return max(inc[N-1], dec[N-1])