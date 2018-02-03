class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        pre = cost[0]
        cur = cost[1]
        for i in range(2, len(cost)):
            pre, cur = cur, min(pre,cur) + cost[i]
        return cur