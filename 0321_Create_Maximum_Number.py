class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # iterate i over 0~k, get first i, k-i element from nums1, nums2
        # get the maximum of i-length sublist from nums1
        # get the maximum of k-i-length sublist from nums2
        # merge two sublist, compare with result
        
        def getMax(nums, l):
            N = len(nums)
            if N < l:
                return []
            ans = []
            for i in range(N):
                # N-i is the length of remain in nums, len(ans) - 1 is the length if we pop
                # If we have more to spend, it is ok to pop. If not, don't pop
                while N - i + len(ans) - 1 >= l and len(ans) > 0 and nums[i] > ans[-1]:
                    ans.pop()
                if len(ans) < l:
                    ans.append(nums[i])
            return ans
        
        def mergeMax(nums1, nums2):
            i = j = 0
            M, N = len(nums1), len(nums2)
            res = []
            while i < M and j < N:
                # if nums1[i] == nums2[j], we need to get to the larger until we stop
                i2, j2 = i, j
                while i2 < M and j2 < N and nums1[i2] == nums2[j2]:
                    i2 += 1
                    j2 += 1
                if i2 == M:
                    res.append(nums2[j])
                    j += 1
                elif j2 == N or nums1[i2] > nums2[j2]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
                    
            while i < M:
                res.append(nums1[i])
                i += 1
            while j < N:
                res.append(nums2[j])
                j += 1
            return res
        
        maxRes = []
        
        for i in range(k+1):
            merge = mergeMax(getMax(nums1, i), getMax(nums2, k-i))
            if len(merge) != k:
                continue
            maxRes = max(maxRes, merge)
        return maxRes