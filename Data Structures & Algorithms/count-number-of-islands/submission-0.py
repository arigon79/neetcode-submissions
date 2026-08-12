class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dx, dy in directions:
                    nx = row + dx
                    ny = col + dy

                    if (min(nx, ny) < 0 or nx >= rows or ny >= cols or grid[nx][ny]=="0"
                    or (nx, ny) in visit):
                        continue
                    q.append((nx, ny))
                    visit.add((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands



        


        