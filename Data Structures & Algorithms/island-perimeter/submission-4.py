class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            perimeter = 0

            while q:
                x, y = q.popleft()

                for dr, dc in directions:
                    nr = x + dr
                    nc = y + dc

                    if (min(nr, nc) < 0 or nr >= ROWS or 
                    nc >= COLS or grid[nr][nc] == 0):
                        perimeter += 1

                    elif (nr, nc) not in visit:
                        q.append((nr, nc))
                        visit.add((nr, nc))
            
            return perimeter
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return bfs(i, j)
        
        return 0

                        
            