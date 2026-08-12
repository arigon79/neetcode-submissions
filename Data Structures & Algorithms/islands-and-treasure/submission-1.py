class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        distances = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        
        def bfs(r, c):
            visit = set()
            q = deque()
            length = 0
            visit.add((r,c))
            q.append((r, c))

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return length
                    for dx, dy in distances:
                        nx, ny = row + dx, col + dy
                        if (nx < 0 or ny < 0 or nx >= rows or ny >= cols 
                            or grid[nx][ny] == -1 or (nx, ny) in visit):
                            continue
                        visit.add((nx, ny))
                        q.append((nx, ny))
                length += 1

            return length

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = min(grid[r][c], bfs(r, c))
        
        return

