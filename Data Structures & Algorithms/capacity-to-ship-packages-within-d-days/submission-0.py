class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cur):
            ships, curCap = 1, cur

            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cur
                
                curCap -= w
            
            return ships <= days

        while l <= r:
            m =  l + (r - l) // 2

            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res


        

