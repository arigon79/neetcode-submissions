class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    res = dp[a - coin]
                    if res != float('inf'):
                        dp[a] = min(dp[a], 1 + res)
        
        return int(dp[amount]) if dp[amount] != float('inf') else -1