class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        def helper(houses: List[int]) -> int:
            rob1, rob2 = 0, 0

            for h in houses:
                tmp = max(rob1 + h, rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        
        res1 = helper(nums[: len(nums) - 1])
        res2 = helper(nums[1: len(nums)])

        return max(res1, res2)
