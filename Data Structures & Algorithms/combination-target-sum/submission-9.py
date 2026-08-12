class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSum, subset):
            nonlocal res

            if curSum > target or i >= len(nums):
                return

            if curSum == target:
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i, curSum + nums[i], subset)

            subset.pop()
            dfs(i + 1, curSum, subset)
            return
        
        dfs(0, 0, [])
        return res