class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []    
        # Time: O(n*2^n)
        # Space: O(2^n)
        def dfs(i, subset):
            nonlocal res

            if i >= len(nums):
                res.append(subset.copy())
                return None
            
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)
            return
        
        dfs(0, [])
        return res