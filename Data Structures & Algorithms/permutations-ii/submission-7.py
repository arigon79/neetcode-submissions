class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i, subset):
            if len(subset) == len(nums):
                val = tuple(nums[k] for k in subset)
                res.add(val)
                
                return 
            
            for j in range(len(nums)):
                if j in subset:
                    continue
                subset.append(j)
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return list(res)

            
            