class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [[] for _ in range(9)]
        col_map = [[] for _ in range(9)]
        sq_map = [[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == '.':
                    continue
                sq_idx = (r // 3)*3 + (c//3)
                if (digit in row_map[r] or digit in col_map[c] or digit in sq_map[sq_idx]):
                    return False
                else:
                    row_map[r].append(digit)
                    col_map[c].append(digit)
                    sq_map[sq_idx].append(digit)
        return True




        
                