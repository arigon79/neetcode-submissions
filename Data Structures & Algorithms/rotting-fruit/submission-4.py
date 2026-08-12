class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        t = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for xr, xc in directions:
                    nr, nc = xr + row, xc + col

                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                            continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
                    
            t += 1
        
        return t if fresh == 0 else -1

