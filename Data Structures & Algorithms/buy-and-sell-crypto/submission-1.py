class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while l < r and r < len(prices):
            currentProf = prices[r] - prices[l]
            if currentProf <=0:
                l = r
                r += 1
            else:
                maxP = max(maxP, currentProf)
                r += 1
        return maxP
        