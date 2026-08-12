class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        piles.sort()
        print(res)
        # [4, 10, 23, 25]
        
        while l <= r:
            k = (l + r) // 2
            print(k)
            times = 0
            for pile in piles:
                times += math.ceil(pile / k)
            
            if times > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)
            
        return res

