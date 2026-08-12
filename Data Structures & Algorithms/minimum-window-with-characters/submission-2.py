class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        res = ''

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i: j]
                valid = True

                for c in set(t):
                    if substring.count(c) < t.count(c):
                        valid = False
                        break
                if valid:
                    if len(res) == 0 or len(substring) < len(res):
                        res = substring

        return res