class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(2^n)
        # Space: O(n)
        memo = {}

        def dfs(i, buying):
            if i == len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                memo[(i, buying)] = max(buy, skip)
            else:
                sell = dfs(i + 1, True) + prices[i]
                skip = dfs(i + 1, False)
                memo[(i, buying)] = max(sell, skip)

            return memo[(i, buying)]            

        return dfs(0, True)
