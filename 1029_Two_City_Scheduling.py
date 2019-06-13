class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # use dp, the other way is to use sort and costs[i][1] - costs[i][0]
        # when dp fill to right, means sending a person to A
        # when dp fill to down, means sending a person to B
        N = len(costs) // 2
        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
        
        for i in range(1, N+1):
            dp[i][0] = dp[i-1][0] + costs[i-1][0]
            
        for j in range(1, N+1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]
            
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i-1][j] + costs[i+j-1][0], dp[i][j-1] + costs[i+j-1][1])

        return dp[N][N]