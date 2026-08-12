class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0

        l, r = 0, len(heights) - 1

        while l < r:
            minBar = min(heights[l], heights[r])
            diff = r - l
            maxAmount = max(maxAmount, (diff * minBar))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxAmount

        