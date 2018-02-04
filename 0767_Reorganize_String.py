class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        sortS = []
        ans = [None] * N
        
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            sortS.extend(c*x)
        ans[::2], ans[1::2] = sortS[N/2:], sortS[:N/2]
        return ''.join(ans)

# The other solution is to use heap that store(count, letter).
# We get top two letter, put into ans, and put the correct count back to the heap.
# This case we don't need to consider the order.


    # def reorganizeString(self, S):
    #     pq = [(-S.count(x), x) for x in set(S)]
    #     heapq.heapify(pq)
    #     if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
    #         return ""

    #     ans = []
    #     while len(pq) >= 2:
    #         nct1, ch1 = heapq.heappop(pq)
    #         nct2, ch2 = heapq.heappop(pq)
    #         if not ans or ch1 != ans[-1]:
    #             ans.extend([ch1, ch2])
    #             if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
    #             if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

    #     return "".join(ans) + (pq[0][1] if pq else '')