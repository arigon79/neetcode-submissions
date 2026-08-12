class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res