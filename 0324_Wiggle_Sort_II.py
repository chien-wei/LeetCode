class Solution:
    def wiggleSort(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        ns = sorted(nums)
        N = len(ns)//2 + len(ns)%2
        ns1, ns2 = ns[:N][::-1], ns[N:][::-1]
        for i in range(len(ns)//2):
            nums[i*2] = ns1[i]
            nums[i*2+1] = ns2[i]
        if len(ns) % 2 == 1:
            nums[-1] = ns1[-1]

# Follow up: 
# Can you do it in O(n) time and/or in-place with O(1) extra space?