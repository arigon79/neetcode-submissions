class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
            or grid[r][c] == 0):
                return 1
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))

            perimeter = 0
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r, c - 1)

            return perimeter

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i, j)
        
        return 0