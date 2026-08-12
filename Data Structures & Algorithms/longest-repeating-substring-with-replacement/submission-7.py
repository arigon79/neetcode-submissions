class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res

        