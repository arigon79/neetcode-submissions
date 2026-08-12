class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.mat = [[0]*(COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.mat[r][c + 1]
                self.mat[r + 1][c + 1] = prefix + above
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.mat[row2][col2]
        above = self.mat[row1 - 1][col2]
        left = self.mat[row2][col1 - 1]
        topLeft = self.mat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""
[0, 0, 0, 0, 0, 0]
[0, 3, 3, 4, 8, 10]
[0, 8, 14, 18, 24, 27]
[0, 9, 17, 21, 28, 36]
[0, 13, 22, 26, 34, 49]
[0, 14, 23, 30, 38, 58]

"""