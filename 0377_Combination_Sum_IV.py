class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # same as coin change II, but now we need all combination
        # so nums should be put in inner loop
        dp = [0 for _ in range(1 + target)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]