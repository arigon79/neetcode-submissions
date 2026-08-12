class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while True:
            if n in visit:
                return False
            visit.add(n)
            n = self.sumSquares(n)
            if n == 1:
                return True
            
    def sumSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        
        return output
