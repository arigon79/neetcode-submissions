class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in  range(9)] 
        cols = [[] for _ in  range(9)] 
        square = [[] for _ in  range(9)] 
        print(cols)
        
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == ".":
                    continue
                sqr_index = math.ceil(i // 3) * 3 + math.ceil(j // 3)
                if (digit in rows[i] or  digit in cols[j] or digit in square[sqr_index]):
                    return False
                else:
                    rows[i].append(digit)
                    cols[j].append(digit)
                    square[sqr_index].append(digit)
        return True