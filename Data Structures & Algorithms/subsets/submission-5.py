class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Time: O(n * 2^n)
        # Space: O(n * 2^n)
        def dfs(i, subset):
            nonlocal res

            if i >= len(nums):
                res.append(subset.copy())
                print(res)
                return

            subset.append(nums[i])
            print(subset)

            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
            return
        
        dfs(0, [])
        return res

