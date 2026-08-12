class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset):
            print(f"subset: {subset}, i = {i}, sum: {sum(subset)}")

            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                print("Res", res)
                return 
                
            if i >= len(candidates) or sum(subset) > target:
                return 
            
            
            subset.append(candidates[i])
            backtrack(i + 1, subset)

            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res