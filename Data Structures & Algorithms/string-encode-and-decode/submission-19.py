class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += f'{n}@{s}'
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        
        while i < len(s):
            while s[j] != '@':
                j += 1
            n = int(s[i: j])
            i = j + 1
            res.append(s[i: i + n])
            i = i + n
            j = i
        return res


