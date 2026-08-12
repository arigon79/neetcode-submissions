class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # t = target
        # m = min(candidates)
        # n = len(candidates)
        # Time: O(n* 2^(n))
        # Space: O(n)
        def dfs(i, curSum, subset):
            nonlocal res

            if curSum == target:
                res.append(subset.copy())
                return None
                
            if i >= len(candidates) or curSum > target:
                return None
                
            subset.append(candidates[i])
            dfs(i + 1, curSum + candidates[i], subset)

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSum, subset)

        dfs(0, 0, [])

        return res