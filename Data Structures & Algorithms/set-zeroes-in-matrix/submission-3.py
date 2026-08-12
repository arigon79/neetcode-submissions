class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_tracker = [False] * rows
        col_tracker = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                        row_tracker[r] = True
                        col_tracker[c] = True
        
        for r in range(rows):
            for c in range(cols):
                if row_tracker[r] or col_tracker[c]:
                    matrix[r][c] = 0
        
        return None
