class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        ans = (n-1) * [float('inf')]
        ans.insert(src,0)
        h = {}
        visit = {src:1}
        #print(ans)
        
        for flight in flights:
            if flight[0] in h:
                h[flight[0]].append([flight[1], flight[2]])
            else:
                h[flight[0]] = [[flight[1], flight[2]]]
        
        for _ in range(K+1):
            new_v = dict(visit)
            for i in visit:
                if i in h:
                    for [d, w] in h[i]:
                        ans[d] = min(ans[d], ans[i] + w)
                        if d not in visit:
                            new_v[d] = 1
                    #print(ans)
            visit = new_v
        return ans[dst] if ans[dst] != float('inf') else -1