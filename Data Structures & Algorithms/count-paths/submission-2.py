class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)] 
        memo[m - 1][n - 1] = 1
        
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[r][c]
        
        return dfs(0, 0)