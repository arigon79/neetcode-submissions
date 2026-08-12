class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            temp = n * curMax
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(curMax, res)

        return res