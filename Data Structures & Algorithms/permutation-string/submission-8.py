class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        n, m = len(s1), len(s2)

        for i in s1:
            count1[i] = count1.get(i, 0) + 1
        
        for j in s2[:n]:
            count2[j] = count2.get(j, 0) + 1

        if count1 == count2:
            return True
        
        for r in range(n, m):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            count2[s2[r - n]] -= 1
            if count2[s2[r - n]] == 0:
                del count2[s2[r - n]]
            
            if count2 == count1:
                return True
        
        return False

        