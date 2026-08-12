class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
            or grid[r][c] == 0):
                print("r", r, "c", c)
                return 0
            
            grid[r][c] = 0
            print(r, c)
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea