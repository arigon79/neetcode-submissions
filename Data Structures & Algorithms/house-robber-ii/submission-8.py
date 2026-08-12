class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_house(num):
            rob1, rob2 = 0, 0
            for n in num:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(rob_house(nums[:-1]), rob_house(nums[1:]))
