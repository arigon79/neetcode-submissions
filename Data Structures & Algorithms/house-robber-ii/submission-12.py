class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # [rob1, rob2, n, n + 1, ...]
        if len(nums) == 1:
            return nums[0]
            
        def robHouse(num):
            rob1, rob2 = 0, 0
            
            for n in num:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(robHouse(nums[:-1]), robHouse(nums[1:]))
