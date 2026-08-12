class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        count = {}
        l, r, res = 0, 0, 0
        while r < len(s):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res

