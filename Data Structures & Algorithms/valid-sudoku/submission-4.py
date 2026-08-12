class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        row_map = [[] for _ in range(rows)]
        col_map = [[] for _ in range(cols)]
        square_map = [[] for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                square_index = (r // 3) * 3 + (c // 3)
                num = board[r][c]
                if num == '.':
                    continue
                if (num in row_map[r] 
                or num in col_map[c] 
                or num in square_map[square_index]):
                    return False
                
                row_map[r].append(num)
                col_map[c].append(num)
                square_map[square_index].append(num)

        return True


