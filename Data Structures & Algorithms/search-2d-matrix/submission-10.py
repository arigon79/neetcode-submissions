class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if target > matrix[rows - 1][cols - 1]:
            return False
        if target < matrix[0][0]:
            return False

        for r in range(rows):
            if target > matrix[r][cols - 1]:
                continue
            else:
                i, j = 0, cols - 1
                while i <= j:
                    mid = i + (j - i) // 2
                    if matrix[r][mid] > target:
                        j = mid - 1
                    elif matrix[r][mid] < target:
                        i = mid + 1
                    else:
                        return True
        return False