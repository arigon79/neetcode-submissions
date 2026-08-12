class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = sorted(s1)
        
        for i in range(len(s2) - n + 1):
            cur = s2[i:i + n]
            if sorted(cur) == s1:
                return True
        return False

