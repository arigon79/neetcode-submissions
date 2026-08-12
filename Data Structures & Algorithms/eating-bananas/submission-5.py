import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid =  l + (r - l) // 2

            totalHours = 0

            for t in piles:
                totalHours += math.ceil(t/ mid)
                
            if totalHours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            