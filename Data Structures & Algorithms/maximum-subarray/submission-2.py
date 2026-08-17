class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        maxSum, curSum = nums[0], 0

        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        
        return maxSum