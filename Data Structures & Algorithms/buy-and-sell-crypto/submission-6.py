class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = l + 1

        while l < len(prices) and r < len(prices):
            if prices[r] - prices[l] <= 0:
                l = r
            else:
                res = max(prices[r] - prices[l], res)
            
            r += 1
        
        return res



        




        