class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = {}
        mx_count = 0
        major = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > mx_count:
                major = num
                mx_count = count[num]
        return mx_count > len(nums) // 2 and target == major