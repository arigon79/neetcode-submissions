class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            if matrix[r][0] > target:
                return False
            if target > matrix[r][cols - 1] :
                continue
            else:
                left, right = 0, cols - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    print(r, mid)
                    if matrix[r][mid] > target:
                        right = mid - 1
                    elif matrix[r][mid] < target:
                        left = mid + 1
                    else:
                        return True
        return False

                
        