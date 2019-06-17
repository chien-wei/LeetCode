class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # two pointer sliding windows
        # need var minLen, curVal, i, j, curLen = j - i + 1
        i, j = 0, 0
        minLen, curVal = float('inf'), 0
        N = len(nums)
        while j < N:
            curVal += nums[j]
            while curVal >= s:
                minLen = min(minLen, j - i + 1)
                curVal -= nums[i]
                i += 1
            j += 1

        return 0 if minLen == float('inf') else minLen