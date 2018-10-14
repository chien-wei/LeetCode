class Solution:
    def nSum(self, nums, target, n, result, results):
        #print(nums, target, n, result, results)
        if len(nums) < n or n < 2:
            return
        if n == 2:
            l, r = 0, len(nums)-1
            while r > l:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                        
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-n+1):
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target - nums[i], n-1, result+[nums[i]], results)
        return
    
    def factorial(n):
        if(n<=1):
            return 1
        else:
            return factorial(n-1) * n
    
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        nc = {}
        for a in A:
            nc[a] = nc.get(a, 0) + 1
        
        # 3 sum
        res = []
        A.sort()
        self.nSum(A, target, 3, [], res)
        
        for r in res:
            tmp = 1
            nc2 = {}
            for n in r:
                nc2[n] = nc2.get(n, 0) + 1
            for n in nc2:
                if nc2[n] == 1:
                    tmp *= nc[n]
                elif nc2[n] == 2:
                    tmp *= nc[n] * (nc[n]-1) / 2
                elif nc2[n] == 3:
                    tmp *= nc[n] * (nc[n]-1) * (nc[n]-2) / 6
            ans += tmp
            ans %= 10**9 + 7
        return int(ans)