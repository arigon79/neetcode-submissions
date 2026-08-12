class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []    
        used = [False] * len(nums)

        def dfs(i, subset):
            nonlocal res

            if len(subset) == len(nums):
                res.append(subset.copy()) #O(n)
                return None
            
            for j in range(len(nums)): # O(n)
                if used[j]:
                    continue

                used[j] = True
                subset.append(nums[j])
                dfs(i + 1, subset)
                subset.pop()
                used[j] = False
                            
            return None
        
        dfs(0, [])
        return res