class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while True:
            if n in visit:
                return False
            visit.add(n)
            sumSq = 0
            for i in str(n):
                sumSq += int(i)**2
            
            if sumSq == 1:
                return True
            else:
                n = sumSq
        return
            