class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for c1 in s:
            count1[c1] += 1
        
        for c2 in t:
            count2[c2] += 1

        return count1 == count2