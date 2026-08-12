class Solution:
    def climbStairs(self, n: int) -> int:
        s = {0: 1, 1:1}

        def climb(n):   
            if n in s:
                return s[n]
            s[n] = climb(n - 1) + climb(n - 2)
            return s[n]
        
        return climb(n)