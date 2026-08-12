from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            perimeter = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if (min(nx, ny) < 0 or nx >= rows or ny >= cols or grid[nx][ny] == 0):
                        perimeter += 1
                    elif (nx, ny) not in visit:
                        visit.add((nx, ny))
                        queue.append((nx, ny))

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return bfs(i, j)

        return 0
