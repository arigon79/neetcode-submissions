class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # O(n! * n^2)
        # O(n! * n)
        def dfs(i, subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in subset:
                    continue
                subset.append(nums[j])
                dfs(i + 1, subset)
                subset.pop()
            return 
        dfs(0, [])
        return res