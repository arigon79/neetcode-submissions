class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2 3 -> 111, 21, 12
        one, two = 1, 1
        
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

