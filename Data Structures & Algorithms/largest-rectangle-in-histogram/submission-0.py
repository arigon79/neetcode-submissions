class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = -float("inf")
        n = len(heights)

        for i in range(n):
            res = max(res, heights[i])
            minHeight = heights[i]
            for j in range(i + 1, n):
                minHeight = min(minHeight, heights[j])
                res = max(res, minHeight * (j - i + 1))
        return res

