class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        if N == 0:
            return 0
        
        mx = [0] * N
        for i in range(N):
            for j in range(max(0, i-K+1), i+1):
                mx[i] = max(mx[i], max(A[j: i+1]) * (i+1 - j) + (mx[j-1] if j-1 >= 0 else 0))
                
        return mx[N-1]