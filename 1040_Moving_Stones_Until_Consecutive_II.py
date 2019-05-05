class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones = sorted(stones)
        N = len(stones)
        mx = max(stones[N-2] - stones[0], stones[N-1] - stones[1]) - N + 2
        
        mn = N
        i = 0
        # sliding window
        for j in range(N):
            while stones[j] - stones[i] + 1 > N:
                i += 1
            already_store = j - i + 1
            # special case: check consecutive sequence
            if already_store == N - 1 and stones[j] - stones[i] + 1 == N - 1:
                mn = min(mn, 2)
            else:
                mn = min(mn, N - already_store)
        
        return [mn, mx]