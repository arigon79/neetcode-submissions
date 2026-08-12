class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n)
        # Space Complexity: O(1)
        l = 0
        r = 1
        res = 0
        while l < r and r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1
        return res