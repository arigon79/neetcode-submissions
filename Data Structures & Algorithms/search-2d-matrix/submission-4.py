class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][-1]:
                l = 0
                r = cols - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if target > matrix[i][mid]:
                        l = mid + 1
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        return True
        return False

