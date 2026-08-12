class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums) - 1:
                return 0

            if nums[i] == 0:
                return float('inf')

            memo[i] = float('inf')
            for j in range(1, nums[i] + 1):
                memo[i] = min(memo[i], 1 + dfs(i + j))
            
            return memo[i]

        return dfs(0)
