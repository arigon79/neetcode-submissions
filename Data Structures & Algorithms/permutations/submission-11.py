class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(i, subset):
            nonlocal res

            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for j in range(len(nums)):
                if used[j] == True:
                    continue
                used[j] = True
                subset.append(nums[j])
                dfs(i + 1, subset)
                subset.pop()
                used[j] = False
            return                
            
        dfs(0, [])
        return res