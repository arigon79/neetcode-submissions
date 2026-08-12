import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q  = deque()
        time, fresh = 0, 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col  = dr + r, dc + c
                    if (min(row, col) < 0 or row >= ROWS or col >= COLS 
                    or grid[row][col] == 0 or grid[row][col] == 2):
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))

            time += 1

        return time if fresh == 0 else -1