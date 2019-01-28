class Solution:
    def wiggleSort(self, nums):
        ns = sorted(nums)
        l = len(ns)
        mi = l // 2 + (1 if l % 2 == 1 else 0)
        fst, snd = ns[:mi], ns[mi:][::-1]
        print(fst, snd)
        res = []
        for i in range(len(snd)):
            res.append(fst[i])
            res.append(snd[i])

        if len(snd) == len(fst)-1:
            res.append(fst[-1])
        return res

s = Solution()
print(s.wiggleSort([3, 5, 2, 1, 6, 4, 7]))