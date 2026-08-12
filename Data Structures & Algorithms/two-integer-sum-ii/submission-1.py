class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(numbers) - 1

        while left < right:
            summation = numbers[left] + numbers[right]
            if summation > target:
                right -= 1
                continue
            if summation < target:
                left += 1
                continue
            if summation == target:
                res.append(left + 1)
                res.append(right + 1)
                break
        
        return res

        