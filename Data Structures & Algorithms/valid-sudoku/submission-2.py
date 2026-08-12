class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_map = [[] for _ in range(rows)]
        cols_map = [[] for _ in range(cols)]
        squares_map = [[] for _ in range(9)]
        
        for row in range(rows):
            for col in range(cols):
                square_index = (row // 3) * 3 + (col // 3)
                num = board[row][col]
                if num == ".":
                    continue
                if num in rows_map[row] or num in cols_map[col] or num in squares_map[square_index]:
                    return False
                rows_map[row].append(num)
                cols_map[col].append(num)
                squares_map[square_index].append(num)

        return True


