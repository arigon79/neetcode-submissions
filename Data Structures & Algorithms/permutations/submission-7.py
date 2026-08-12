class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in subset:
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])           
        return res
