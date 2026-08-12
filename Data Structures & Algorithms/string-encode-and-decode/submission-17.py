class Solution:

    def encode(self, strs: List[str]) -> str:
        res  = ''

        for s in strs:
            n = str(len(s))
            res += n + '#' + s
        
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1
            

            n = int(s[i:j])

            res.append(s[j + 1: j + 1 + n])
            i = j + 1 + n

        return res

        

        
