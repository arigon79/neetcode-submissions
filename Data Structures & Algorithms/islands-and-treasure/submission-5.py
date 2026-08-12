class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Time: O((m * n)^2)
        # Space: O(m * n)
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit = set()
            visit.add((r, c))
            length = 0

            while q:
                
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        return length
                    
                    for xr, xc in directions:
                        nr, nc = row + xr, col + xc

                        if (nr < 0 or nc < 0 or 
                        nr >= ROWS or nc >= COLS 
                        or grid[nr][nc] == -1 or (nr, nc) in visit):
                            continue

                        visit.add((nr, nc))
                        q.append((nr, nc)) 
                length += 1
            
            return INF


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
        return