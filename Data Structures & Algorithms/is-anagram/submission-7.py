class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity: O(n + m)
        # space complexity: O(1)
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)