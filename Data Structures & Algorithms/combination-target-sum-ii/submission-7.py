class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset):
            print(f"subset: {subset}, i = {i}, sum: {sum(subset)}")

            if sum(subset) == target:
                res.append(subset.copy())
                print("Res", res)
                return 

            if i >= len(candidates) or sum(subset) > target:
                return 
            
            
            subset.append(candidates[i])
            backtrack(i + 1, subset)

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res