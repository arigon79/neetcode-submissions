class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        def dfs(n):      
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 3) + dfs(n - 2) + dfs(n - 1)

            return memo[n]
        
        return dfs(n)