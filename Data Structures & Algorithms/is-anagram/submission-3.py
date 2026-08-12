class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = {}
        freq2 = {}
        
        for i in s:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1

        for j in t:
            if j not in freq2:
                freq2[j] = 1
            else:
                freq2[j] += 1
        
        return freq1 == freq2
