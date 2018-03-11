class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        AA = A + A
        ans = 0
        mCount = 0
        #print(AA)
        for i in range(N):
            count = 0
            for j in range(N):
                #print(i, j)
                if AA[i+j] <= j:
                    count += 1
            if count > mCount:
                ans = i
                mCount = count
            if count >= N - 1:
                break
        return ans