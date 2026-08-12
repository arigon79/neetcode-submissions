class Solution:
    def climbStairs(self, n: int) -> int:
        
        def memorization(i, cache):
            if i > n:
                return 0
            if i == n:
                return 1

            if i in cache:
                return cache[i]
            
            cache[i] = memorization(i + 1, cache) + memorization(i + 2, cache)

            return cache[i]

        return memorization(0, {})
            

            
        