class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, curSum):
            if i == len(nums):
                return 1 if curSum == target else 0
            
            curNum = nums[i]
            return dfs(i + 1, curSum + curNum) + dfs(i + 1, curSum - curNum)

        return dfs(0, 0)
