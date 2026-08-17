class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        # Time: O(mn)
        # Space: O(mn)
        
        def dfs(i, j):
            if (i < 0 or j < 0 or i >= m or j >= n):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if [i, j] == [m - 1, n - 1]:
                return 1
        
            total = dfs(i + 1, j) # rows
            total += dfs(i, j + 1) # cols
            memo[(i, j)] = total
            return total

        return dfs(0, 0)