class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = i + 1

        while i < j and j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                res = max(profit, res)
            else:
                i = j
            j += 1
        
        return res
        


        




        