class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):
                
                topLeft = matrix[top][left + i]

                #switching top left with bottom left
                matrix[top][left + i] = matrix[bottom - i][left]

                # switching bottom left with bottom right
                matrix[bottom -i][left] = matrix[bottom][right - i]

                # switching bottom right with top right
                matrix[bottom][right - i] = matrix[top + i][right]

                # switching top right with top left
                matrix[top + i][right] = topLeft
             
            left += 1
            right -= 1
        
        return None

        