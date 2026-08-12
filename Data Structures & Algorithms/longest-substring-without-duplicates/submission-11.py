class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            res = max(res, r - l + 1)
        return res