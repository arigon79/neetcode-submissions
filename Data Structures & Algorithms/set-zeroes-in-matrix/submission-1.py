class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    continue
                else:
                    # do the top
                    for i in range(r - 1, -1, -1):
                        if matrix[i][c] != 0:
                            matrix[i][c] = '@'
                    # do the right
                    for i in range(c + 1, len(matrix[0])):
                        if matrix[r][i] != 0:
                            matrix[r][i] = '@'
                    # do the left
                    for i in range(c - 1, -1, -1):
                        if matrix[r][i] != 0:
                            matrix[r][i] = '@' 
                        # do the bottom
                    for i in range(r + 1, len(matrix)):
                        if matrix[i][c] != 0:
                            matrix[i][c] = '@'
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '@':
                    matrix[r][c] = 0
        return None
        