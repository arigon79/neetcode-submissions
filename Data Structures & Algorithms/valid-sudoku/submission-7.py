class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        sqr = [[] for _ in range(9)] 

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                sqr_idx = math.floor(r/3) * 3 + math.floor(c/3)
                
                if (num in rows[r] or num in cols[c] or num in sqr[sqr_idx]):
                    return False
                rows[r].append(num)
                cols[c].append(num)
                sqr[sqr_idx].append(num)
        return True
                