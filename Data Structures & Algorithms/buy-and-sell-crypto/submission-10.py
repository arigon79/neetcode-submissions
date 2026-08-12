class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        profit = 0
        while r < len(prices):
            while r < len(prices) and prices[l] >= prices[r]:
                l += 1
                r = l + 1
            while r < len(prices) and prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        
        return profit