class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, = 0, 1
        res = 0

        while l < r and r < len(prices):
            currentProfit = prices[r] - prices[l]
            if currentProfit < 0:
                l = r
            r += 1

            res = max(currentProfit, res)
        
        return res