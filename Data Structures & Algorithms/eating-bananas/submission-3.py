import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = max(piles)

        while start <= end:
            speed = (start + end) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/speed)
            if total_hours > h:
                start = speed + 1
            else:
                end = speed - 1
                res = min(speed, res)
        
        return res
