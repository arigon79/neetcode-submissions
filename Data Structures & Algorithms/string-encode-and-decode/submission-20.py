class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += f'{n}#{s}'
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            n = int(s[l:r])
            string = s[r + 1: r + n + 1]
            res.append(string)
            l = r + n + 1
        return res
            