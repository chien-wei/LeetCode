from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # we only need min1, min2, and index1 in case of next min has same index
        min1, min2, ind1 = 0, 0, -1
        for i in range(len(costs)):
            m1 = m2 = float('inf')
            i1 = -1
            for j in range(len(costs[i])):
                cost = costs[i][j] + (min1 if j != ind1 else min2)
                if cost < m1:
                    m1, m2, i1 = cost, m1, j
                elif cost < m2:
                    m2 = cost
            min1, min2, ind1 = m1, m2, i1
        return min1


s = Solution()
assert s.minCost([[14,2,11],[11,14,5],[14,3,10]]) == 10
assert s.minCost([[5]]) == 5