class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        # Time:  O(2*(t/m))
        # Space:  O(2*(t/m))
        
        def dfs(i, curSum, subset):
            if i >= len(nums) or curSum > target:
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