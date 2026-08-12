class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquares(n)
        
        while slow != fast:
            fast = self.sumSquares(fast)
            fast = self.sumSquares(fast)
            slow = self.sumSquares(slow)
        
        return True if fast == 1 else False
            
            
    def sumSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        
        return output
