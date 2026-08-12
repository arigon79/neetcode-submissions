class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  
        
        for num in numbers:
            summation = numbers[l] + numbers[r]
            if summation < target:
                l += 1
                continue

            if summation > target:
                r -= 1
                continue
            
            if summation == target:
                return [l + 1, r + 1]

            l += 1
            r -= 1
        return []
