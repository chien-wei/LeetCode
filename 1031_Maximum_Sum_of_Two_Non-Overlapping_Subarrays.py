class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # we need to take M + L as the length of sliding windows
        # take max windows of length L and M repectively
        # make sure the other windows is always after the one we have
        B = A[:]
        for i in range(1, len(B)):
            B[i] += B[i-1]
        res, Lmax, Mmax = B[L + M - 1], B[L - 1], B[M - 1]
        for i in range(L+M, len(B)):
            print(res, Lmax, Mmax)
            Lmax = max(Lmax, B[i - M] - B[i - M - L])
            Mmax = max(Mmax, B[i - L] - B[i - L - M])
            res = max(res, Lmax + B[i] - B[i - M], Mmax + B[i] - B[i - L])
        return res