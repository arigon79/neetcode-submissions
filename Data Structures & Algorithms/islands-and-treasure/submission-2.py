class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647

        def bfs(r, c):
            visit = set()
            q = deque()
            length = 0
            visit.add((r, c))
            q.append((r, c))

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        return length
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS
                        or grid[nr][nc] == -1 or (nr, nc) in visit):
                            continue
                        
                        q.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
            
            return length

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = min(grid[i][j], bfs(i, j))
        
        return None