# sorting solution
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums.sort()
        index = 1
        ans = 1
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] >= index:
                index += 1
            if nums[i] > index:
                ans = index
                break
        if index == nums[-1]:
            ans = index + 1
        return ans


# linear time, constant space solution
# using element value as index
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def remove_unwanted(A):
            for i in range(len(A))[::-1]:
                if A[i] < 1:
                    A.pop(i)
            
        remove_unwanted(nums)
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if j < len(nums) and j >= 0:
                nums[j] = -abs(nums[j])
                
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums) + 1