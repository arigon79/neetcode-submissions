class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                x, y = q.popleft()

                for dr, dc in directions:
                    nr, nc = x + dr, y + dc

                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS
                    or grid[nr][nc] == "0" or (nr, nc) in visit):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
                    

        