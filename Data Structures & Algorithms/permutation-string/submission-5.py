class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        l = 0
        r = l + len(s1)

        while r <= len(s2):
            cur_str = s2[l:r]
            count2 = {}
            for c in cur_str:
                count2[c] = count2.get(c, 0) + 1
            
            if count1 == count2:
                return True
            
            l += 1
            r = l + len(s1)
        
        return False