class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        c1 = Counter(s1)
        
        for i in range(len(s2)):
            c2 = Counter(s2[i: i + n])
            if c1 == c2:
                return True
        return False