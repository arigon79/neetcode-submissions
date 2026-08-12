class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        res = 0
        l, r = 0, 1
        while l < r and r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1
        return res