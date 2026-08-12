class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1
        if n == 0:
            return one
        elif n == 1:
            return two
        elif n == 2:
            return three
        
        for _ in range(n - 2):
            temp = three
            three = one + two + three
            one = two
            two = temp
        
        return three
            

            