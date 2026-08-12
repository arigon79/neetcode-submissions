class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
                
        def dfs(r, c):
            nonlocal res

            if r == m - 1 and c == n - 1:
                res += 1
                return 
            
            if r + 1 < m:
                dfs(r + 1, c)
            
            if c + 1 < n:
                dfs(r, c + 1)
                
            return 
        
        dfs(0, 0)
        return res
                