class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(0, amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
        return dp[len(coins)][amount]

# better dp
# if coins iterate in inner loop, it count more than one time
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        return dp[amount]